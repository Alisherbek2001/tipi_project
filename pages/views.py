from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
)
from .models import Pages
from .serializers import PagesCreateUpdateSerializer, PagesRetrieveSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from common.permissions import IsSuperAdmin


class PagesListCreateAPIView(ListCreateAPIView):
    queryset = Pages.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return PagesCreateUpdateSerializer
        return PagesRetrieveSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated, IsSuperAdmin]
        return [permission() for permission in permission_classes]


class PagesRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Pages.objects.all()
    permission_classes = [IsAuthenticated, IsSuperAdmin]

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return PagesCreateUpdateSerializer
        return PagesRetrieveSerializer


class PagesListAPIView(ListAPIView):
    queryset = Pages.objects.all()
    serializer_class = PagesRetrieveSerializer

    def get_permissions(self):
        return [AllowAny()]

    def get_queryset(self):
        queryset = super().get_queryset()
        pages_param = self.request.query_params.get("pages")
        if pages_param:
            queryset = queryset.filter(pages=pages_param)
        return queryset
