from rest_framework import status, views, generics
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from dbc_conference.dbc_conference import settings
from dbc_conference.users.api.serializers import \
    UserRegistrationSerializer, UserLoginSerializer, ThirdPartySerializer, BusinessCardSerializer
from dbc_conference.users.models import User, ThirdParty, BusinessCard


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
        _phone = serializer.data['phone']
        _token = serializer.data['token']
        _user = User.objects.get(phone=_phone)
        _role = _user.status
        settings.DB_LOGIN, settings.DB_PASS = settings.change_root(_role)
        print(settings.DB_LOGIN)
        return Response({'role': _role,
                         'token': _token,
                         'phone': _phone},
                        status=status.HTTP_200_OK)

    def get_queryset(self):
        return


class CreateBusinessCardView(views.APIView):
    def post(self, request):
        user = self.request.user
        data = request.data
        data['user'] = user
        serializer = BusinessCardSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserBusinessCardView(views.APIView):
    def get(self, request, pk):
        business_card = BusinessCard.objects.get_object_or_none(user__id=pk)
        serializer = BusinessCardSerializer(data=business_card)
        if business_card is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # some shit here
        if serializer.is_valid(raise_exception=True):
            return Response(data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class CreateThirdPartyView(views.APIView):
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
    serializer_class = ThirdPartySerializer
    queryset = ThirdParty.objects.all()