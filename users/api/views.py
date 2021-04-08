from rest_framework import status, views, generics
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from dbc_conference import settings
from users.api.serializers import \
    UserRegistrationSerializer, UserLoginSerializer, ThirdPartySerializer, BusinessCardSerializer
from users.models import User, ThirdParty, BusinessCard


class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)


class UserLoginView(ListAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        serializer.validate(request.data)
        _email = serializer.data['email']
        _token = serializer.data['token']
        _user = User.objects.get(email=_email)
        _role = _user.status
        settings.DB_LOGIN, settings.DB_PASS = settings.change_root(_role)
        print(settings.DB_LOGIN)
        return Response({'role': _role,
                         'token': _token,
                         'email': _email},
                        status=status.HTTP_200_OK)

    def get_queryset(self):
        return


class CreateBusinessCardView(views.APIView):
    authentication_classes = [JSONWebTokenAuthentication, ]

    def post(self, request):
        user = self.request.user.id
        data = request.data
        data['user'] = user
        serializer = BusinessCardSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserBusinessCardView(views.APIView):
    permission_classes = [AllowAny, ]

    def get(self, request, pk):
        business_card = BusinessCard.objects.get(user__id=pk)
        if business_card is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BusinessCardSerializer(business_card, many=False)
        return Response(data=serializer.data)
        #return Response(status=status.HTTP_400_BAD_REQUEST)


class CreateThirdPartyView(views.APIView):
    authentication_classes = [JSONWebTokenAuthentication, ]

    def post(self, request):
        user = self.request.user
        data = request.data
        data['user'] = user
        serializer = ThirdPartySerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ThirdPartyListView(generics.ListAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = ThirdPartySerializer
    queryset = ThirdParty.objects.all()
