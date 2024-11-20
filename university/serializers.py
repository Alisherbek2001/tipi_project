from rest_framework import serializers
from .models import AboutUniversity


class AboutUniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUniversity
        fields = [
            "id",
            "title_uz",
            "title_ru",
            "title_en",
            "is_active",
            "created_at",
            "updated_at",
        ]
