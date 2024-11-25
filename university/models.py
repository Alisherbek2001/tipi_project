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

    # teachers = models.ManyToManyField("teachers.Teacher")

    def __str__(self) -> str:
        return self.title_uz


class FacultyDirection(BaseModel):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255, null=True, blank=True)
    title_en = models.CharField(max_length=255, null=True, blank=True)
    stage_uz = models.CharField(max_length=255, null=True, blank=True)
    stage_ru = models.CharField(max_length=255, null=True, blank=True)
    stage_en = models.CharField(max_length=255, null=True, blank=True)
    duration_uz = models.CharField(max_length=255, null=True, blank=True)
    duration_ru = models.CharField(max_length=255, null=True, blank=True)
    duration_en = models.CharField(max_length=255, null=True, blank=True)
    department_uz = models.CharField(max_length=255, null=True, blank=True)
    department_ru = models.CharField(max_length=255, null=True, blank=True)
    department_en = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title_uz


class Student(BaseModel):
    name = models.CharField(max_length=255)
    telegram = models.CharField(max_length=255, null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    youtube = models.CharField(max_length=255, null=True, blank=True)
    description_uz = models.TextField(null=True, blank=True)
    description_ru = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
