from django.db import models
from common.models import BaseModel
from common.models import Image, File


class Pages(BaseModel):
    title_uz = models.CharField(max_length=255, null=True, blank=True)
    title_ru = models.CharField(max_length=255, null=True, blank=True)
    title_en = models.CharField(max_length=255, null=True, blank=True)
    description_uz = models.TextField(null=True, blank=True)
    description_ru = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    images = models.ManyToManyField(Image, blank=True)
    files = models.ManyToManyField(File, blank=True)
    link1 = models.CharField(max_length=255, null=True, blank=True)
    link2 = models.CharField(max_length=255, null=True, blank=True)
    pages = models.CharField(max_length=255)
