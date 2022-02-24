from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "other_name",
            "email",
            "phone",
            "birthday",
            "is_admin"
        ]
        extra_kwargs = {'password': {'write_only': True}}


class ShortUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email"]


class PrivateShortUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
