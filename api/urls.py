from django.urls import path
from .views import *


urlpatterns = [
    path("image/", CreateImageAPIView.as_view(), name="create-image"),
    path("video/", CreateVideoAPIView.as_view(), name="create-video"),
    path("file/", CreateFileAPIView.as_view(), name="create-file"),
]
