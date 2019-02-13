from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _
from rest_framework.exceptions import ValidationError

from yatla.follows.models import Follow
from yatla.users.models import User


class FollowSerializer(serializers.ModelSerializer):
    follows = serializers.CharField(help_text=_("username of the user to follow"))

    class Meta:
        model = Follow
        fields = ["id", "user", "follows", "created"]
        extra_kwargs = {
            "user": {"read_only": True}
        }

    def validate_follows(self, value):
        try:
            follows = User.objects.get(username=value)
            return follows
        except User.DoesNotExist:
            raise ValidationError("User to follow not found")
