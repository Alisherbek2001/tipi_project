from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import AboutUniversity, Adminstration, Department
from .serializers import (
    AboutUniversitySerializer,
    AdminstrationSerializer,
    DepartmentSerializer,
)
from common.permissions import IsSuperAdmin


class AboutUniversityViewSet(ModelViewSet):
    queryset = AboutUniversity.objects.all()
    serializer_class = AboutUniversitySerializer
    permission_classes = [
        IsAuthenticated,
        IsSuperAdmin,
    ]

    def perform_create(self, serializer):
        serializer.save()


class AdminstrationViewSet(ModelViewSet):
    queryset = Adminstration.objects.all()
    serializer_class = AdminstrationSerializer
    permission_classes = [
        IsAuthenticated,
        IsSuperAdmin,
    ]

    def perform_create(self, serializer):
        serializer.save()


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [
        IsAuthenticated,
        IsSuperAdmin,
    ]

    def perform_create(self, serializer):
        serializer.save()
