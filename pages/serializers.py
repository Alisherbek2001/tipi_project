from rest_framework import serializers
from .models import Pages
from common.models import Image, File
from common.serializers import ImageSerializer, FileSerializer


class PagesCreateUpdateSerializer(serializers.ModelSerializer):
    images = serializers.PrimaryKeyRelatedField(
        queryset=Image.objects.all(), many=True, required=False
    )
    files = serializers.PrimaryKeyRelatedField(
        queryset=File.objects.all(), many=True, required=False
    )

    class Meta:
        model = Pages
        fields = "__all__"


class PagesRetrieveSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    files = FileSerializer(many=True)

    class Meta:
        model = Pages
        fields = "__all__"
