from django.db import models
from common.models import BaseModel


class Murojat(BaseModel):
    name = models.CharField(max_length=255)
    description_uz = models.TextField()
    description_ru = models.TextField()
    description_en = models.TextField()
    phone = models.CharField(max_length=255)
    status = models.CharField(max_length=255, default="Kutilmoqda")

    def __str__(self) -> str:
        return self.name
