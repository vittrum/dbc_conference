from rest_framework import serializers

from ..models import Thesis, ThesisReview


class ThesisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thesis
        fields = '__all__'


class ThesisReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThesisReview
        fields = '__all__'
