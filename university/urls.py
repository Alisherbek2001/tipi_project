from rest_framework.routers import DefaultRouter
from .views import AboutUniversityViewSet
from django.urls import path
from .views import AboutUniversityViewSet

urlpatterns = [
    path(
        "about-university/",
        AboutUniversityViewSet.as_view(
            {
                "get": "list",  # Barcha obyektlarni ko'rish
                "post": "create",  # Yangi obyekt qo'shish
            }
        ),
        name="about-university-list",
    ),
    path(
        "about-university/<int:pk>/",
        AboutUniversityViewSet.as_view(
            {
                "get": "retrieve",  # Bitta obyektni ko'rish
                "put": "update",  # To'liq o'zgartirish
                "patch": "partial_update",  # Qisman o'zgartirish
                "delete": "destroy",  # O'chirish
            }
        ),
        name="about-university-detail",
    ),
]
