from django.db import models
from common.models import BaseModel
from common.models import Image


class AboutUniversity(BaseModel):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255, null=True, blank=True)
    title_en = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title_uz


class Adminstration(BaseModel):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255, null=True, blank=True)
    title_en = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title_uz


class Department(BaseModel):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255, null=True, blank=True)
    title_en = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title_uz


class Faculty(BaseModel):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255, null=True, blank=True)
    title_en = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title_uz
