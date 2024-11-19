from django.db import models
from common.models import BaseModel


class Pages(BaseModel):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
