from rest_framework import serializers
from .models import AboutUniversity, Adminstration, Department, Faculty
from common.models import Image
from common.serializers import ImageSerializer


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


class FacultyCreateSerializer(serializers.ModelSerializer):
    image = serializers.PrimaryKeyRelatedField(
        queryset=Image.objects.all(), required=True
    )

    class Meta:
        model = Faculty
        fields = "__all__"


class FacultySerializer(serializers.ModelSerializer):
    image = ImageSerializer()

    class Meta:
        model = Faculty
        fields = "__all__"


class FacultyRetrieveSerializer(serializers.ModelSerializer):
    image = ImageSerializer()

    class Meta:
        model = Faculty
        fields = "__all__"
