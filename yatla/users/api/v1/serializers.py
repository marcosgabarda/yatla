from django.contrib.auth.hashers import make_password
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from yatla.users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer to handle users."""

    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "password"]
        extra_kwargs = {"password": {"write_only": True, "required": False}}

    def validate_password(self, value):
        value = make_password(value)
        return value


class PublicUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ["id", "username", "first_name", "last_name"]
