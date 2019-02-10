from rest_framework import serializers

from yatla.follows.models import Follow


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ["id", "user", "follows", "created"]
