from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import (
    AboutUniversity,
    Adminstration,
    Department,
    Faculty,
    FacultyDirection,
    Student,
)
from .serializers import (
    AboutUniversitySerializer,
    AdminstrationSerializer,
    DepartmentSerializer,
    FacultyCreateSerializer,
    FacultyDirectionSerializer,
    FacultyRetrieveSerializer,
    FacultySerializer,
    StudentCreateSerializer,
    StudentRetrieveSerializer,
    StudentSerializer,
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

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated, IsSuperAdmin]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save()


class AdminstrationViewSet(ModelViewSet):
    queryset = Adminstration.objects.all()
    serializer_class = AdminstrationSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated, IsSuperAdmin]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save()


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated, IsSuperAdmin]
        return [permission() for permission in permission_classes]

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
    permission_classes = [IsAuthenticated, IsSuperAdmin]
    queryset = Faculty.objects.all()
    serializer_class = FacultyRetrieveSerializer


class FacultyAPIView(ListAPIView):
    permission_classes = [IsAuthenticated, IsSuperAdmin]
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


class FacultyDirectionViewSet(ModelViewSet):
    queryset = FacultyDirection.objects.all()
    serializer_class = FacultyDirectionSerializer
    permission_classes = [IsAuthenticated, IsSuperAdmin]


class StudentCreateAPIView(APIView):
    permission_classes = [IsAuthenticated, IsSuperAdmin]

    def post(self, request):
        serializer = StudentCreateSerializer(data=request.data)

        if serializer.is_valid():
            student = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentRetrieveAPIView(RetrieveAPIView, DestroyAPIView):
    permission_classes = [IsAuthenticated, IsSuperAdmin]
    queryset = Student.objects.all()
    serializer_class = StudentRetrieveSerializer


class StundentAPIView(ListAPIView):
    permission_classes = [IsAuthenticated, IsSuperAdmin]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated, IsSuperAdmin]
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
