from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import AboutUniversity, Adminstration, Department, Faculty
from .serializers import (
    AboutUniversitySerializer,
    AdminstrationSerializer,
    DepartmentSerializer,
    FacultyCreateSerializer,
    FacultyRetrieveSerializer,
    FacultySerializer,
)
from common.permissions import IsSuperAdmin
from rest_framework.generics import (
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
)
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class AboutUniversityViewSet(ModelViewSet):
    queryset = AboutUniversity.objects.all()
    serializer_class = AboutUniversitySerializer
    permission_classes = [IsAuthenticated, IsSuperAdmin]

    def perform_create(self, serializer):
        serializer.save()


class AdminstrationViewSet(ModelViewSet):
    queryset = Adminstration.objects.all()
    serializer_class = AdminstrationSerializer
    permission_classes = [IsAuthenticated, IsSuperAdmin]

    def perform_create(self, serializer):
        serializer.save()


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated, IsSuperAdmin]

    def perform_create(self, serializer):
        serializer.save()


class FacultyCreateAPIView(APIView):
    permission_classes = [IsAuthenticated, IsSuperAdmin]

    def post(self, request):
        serializer = FacultyCreateSerializer(data=request.data)

        if serializer.is_valid():
            faculty = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FacultyRetrieveAPIView(RetrieveAPIView, DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Faculty.objects.all()
    serializer_class = FacultyRetrieveSerializer


class FacultyAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class FacultyUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated, IsSuperAdmin]
    queryset = Faculty.objects.all()
    serializer_class = FacultyCreateSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
