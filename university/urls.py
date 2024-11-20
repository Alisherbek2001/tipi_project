from .views import (
    AboutUniversityViewSet,
    AdminstrationViewSet,
    DepartmentViewSet,
    FacultyCreateAPIView,
    FacultyRetrieveAPIView,
    FacultyAPIView,
    FacultyUpdateAPIView,
    FacultyDirectionViewSet,
    StudentCreateAPIView,
    StudentRetrieveAPIView,
    StundentAPIView,
    StudentUpdateAPIView,
)
from django.urls import path

urlpatterns = [
    path(
        "about-university/",
        AboutUniversityViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="about-university-list",
    ),
    path(
        "about-university/<int:pk>/",
        AboutUniversityViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="about-university-detail",
    ),
    path(
        "adminstration/",
        AdminstrationViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="adminstration-list",
    ),
    path(
        "adminstration/<int:pk>/",
        AdminstrationViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="adminstration-detail",
    ),
    path(
        "department/",
        DepartmentViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="department-list",
    ),
    path(
        "department/<int:pk>/",
        DepartmentViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="department-detail",
    ),
    path(
        "faculty/",
        FacultyCreateAPIView.as_view(),
        name="faculty-create",
    ),
    path("faculty/all/", FacultyAPIView.as_view(), name="all-faculty"),
    path(
        "faculty/<int:pk>/",
        FacultyRetrieveAPIView.as_view(),
        name="faculty-detail",
    ),
    path(
        "faculty/<int:pk>/update/",
        FacultyUpdateAPIView.as_view(),
        name="faculty-update",
    ),
    path(
        "faculty/direction",
        FacultyDirectionViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="faculty-direction-list",
    ),
    path(
        "faculty/direction/<int:pk>",
        FacultyDirectionViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="faculty-direction-detail",
    ),
    path(
        "students/", StundentAPIView.as_view(), name="student-list"
    ),  # Barcha talabalar ro'yxati
    path(
        "students/create/", StudentCreateAPIView.as_view(), name="student-create"
    ),  # Talaba yaratish
    path(
        "students/<int:pk>/", StudentRetrieveAPIView.as_view(), name="student-detail"
    ),  # Talaba haqida ma'lumot
    path(
        "students/<int:pk>/update/",
        StudentUpdateAPIView.as_view(),
        name="student-update",
    ),  # Talabani o'zgartirish
]
