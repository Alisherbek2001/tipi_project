from rest_framework import serializers
from .models import AboutUniversity, Adminstration, Department


class AboutUniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUniversity
        fields = "__all__"


class AdminstrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adminstration
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"
