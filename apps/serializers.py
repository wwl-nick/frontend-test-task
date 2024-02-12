from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

from apps.models import Platform, App


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = '__all__'


class AppSerializer(serializers.ModelSerializer):
    icon = Base64ImageField()

    class Meta:
        model = App
        fields = '__all__'
        read_only_fields = ('author', 'created_at')
