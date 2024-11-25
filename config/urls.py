from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("users.urls")),
    path("", include("university.urls")),
    path("", include("common.urls")),
    path("", include("appeal.urls")),
    path("", include("pages.urls")),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
