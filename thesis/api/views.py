from rest_framework import generics, views, status
from rest_framework.response import Response

from .serializers import ThesisSerializer, ThesisReviewSerializer
from ..models import Thesis


class CreateThesisView(views.APIView):
    def post(self, request):
        data = request.data
        data['user'] = self.request.user
        serializer = ThesisSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(status=status.HTTP_201_CREATED)


class ReleaseThesisView(views.APIView):
    def post(self, request, pk):
        thesis = Thesis.objects.get_object_or_404(id=pk)
        thesis.draft = False
        thesis.save()
        return Response(status=status.HTTP_200_OK)


class HideThesisView(views.APIView):
    def post(self, request, pk):
        thesis = Thesis.objects.get_object_or_404(id=pk)
        thesis.draft = True
        thesis.save()
        return Response(status=status.HTTP_200_OK)


class UpdateThesisView(generics.UpdateAPIView):
    serializer_class = ThesisSerializer
    queryset = Thesis.objects.all()


class ListThesisView(generics.ListAPIView):
    serializer_class = ThesisSerializer
    queryset = Thesis.objects.filter(draft=False)


class CreateThesisReviewView(views.APIView):
    def post(self, request, pk):
        data = request.data
        data['user'] = self.request.user
        data['thesis'] = Thesis.objects.get_object_or_404(id=pk)
        serializer = ThesisReviewSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(status=status.HTTP_201_CREATED)


class ListUserThesisView(generics.ListAPIView):
    serializer_class = ThesisSerializer

    def get_queryset(self):
        user = self.request.user
        return Thesis.objects.filter(user=user)