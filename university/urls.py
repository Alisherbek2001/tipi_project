from .views import AboutUniversityViewSet, AdminstrationViewSet
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
]
