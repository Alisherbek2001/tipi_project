from django.urls import path
from .views import ImageAPIView

urlpatterns = [
    path("create/image/", ImageAPIView.as_view(), name="create-image"),
]
