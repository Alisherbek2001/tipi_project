from django.urls import path
from .views import (
    PagesListCreateAPIView,
    PagesRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path("pages/", PagesListCreateAPIView.as_view(), name="pages-list-create"),
    path(
        "pages/<int:pk>/",
        PagesRetrieveUpdateDestroyAPIView.as_view(),
        name="pages-retrieve-update-destroy",
    ),
]
