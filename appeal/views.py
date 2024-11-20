from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Murojat

# class MurojatViewSet(ModelViewSet):
#     queryset = Murojat.objects.all()
#     serializer_class = AboutUniversitySerializer
#     permission_classes = [IsAuthenticated, IsSuperAdmin]

#     def perform_create(self, serializer):
#         serializer.save()
