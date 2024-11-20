from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import AboutUniversity
from .serializers import AboutUniversitySerializer
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
