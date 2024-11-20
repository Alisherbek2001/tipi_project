from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from common.permissions import IsSuperAdmin
from rest_framework.viewsets import ModelViewSet
from .models import Murojat
from .serializers import MurojatSerializer


class MurojatViewSet(ModelViewSet):
    queryset = Murojat.objects.all()
    serializer_class = MurojatSerializer

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [AllowAny]
        else:
            permission_classes = [
                IsAuthenticated,
                IsSuperAdmin,
            ]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save()
