from rest_framework import serializers
from utility.models import *


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["id", "image"]


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ["id", "type", "link", "video"]


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ["id", "file"]
