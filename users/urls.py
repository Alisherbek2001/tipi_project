from django.urls import path
from .views import CreateUserView, ChangePasswordView

urlpatterns = [
    path("create-user/", CreateUserView.as_view(), name="create_user"),
    path("change-password/", ChangePasswordView.as_view(), name="change_password"),
]
