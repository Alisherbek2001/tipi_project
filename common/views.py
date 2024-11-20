from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from .models import Image, File
from .serializers import ImageSerializer, FileSerializer
from rest_framework.generics import CreateAPIView
from .permissions import IsSuperAdmin


class ImageAPIView(CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated, IsSuperAdmin]


class FileAPIView(CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticated, IsSuperAdmin]
