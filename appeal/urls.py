from django.urls import path
from .views import MurojatViewSet

urlpatterns = [
    path(
        "murojat/",
        MurojatViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="murojat-list",
    ),
    path(
        "murojat/<int:pk>/",
        MurojatViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="murojat-detail",
    ),
]
