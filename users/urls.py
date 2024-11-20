from django.urls import path
from .views import (
    CreateUserView,
    ChangePasswordView,
    AdminsListAPIView,
    DeleteUserAPIView,
)
from .views import CustomTokenObtainPairView


urlpatterns = [
    path("api/token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("create-user/", CreateUserView.as_view(), name="create_user"),
    path("change-password/", ChangePasswordView.as_view(), name="change_password"),
    path("admin-list/", AdminsListAPIView.as_view(), name="admin-list"),
    path("delete-user/<int:user_id>/", DeleteUserAPIView.as_view(), name="delete-user"),
]
