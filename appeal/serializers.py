from rest_framework import serializers
from .models import Murojat


class MurojatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Murojat
        fields = "__all__"
