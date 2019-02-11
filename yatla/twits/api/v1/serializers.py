from rest_framework import serializers

from yatla.twits.models import Twit, Like, ReTwit
from yatla.users.api.v1.serializers import PublicUserSerializer


class TwitSerializer(serializers.ModelSerializer):
    user = PublicUserSerializer(read_only=True)

    class Meta:
        model = Twit
        fields = ["id", "user", "text", "likes", "retwits", "created"]


class LikeSerializer(serializers.ModelSerializer):
    user = PublicUserSerializer(read_only=True)

    class Meta:
        model = Like
        fields = ["id", "user", "twit", "created"]


class ReTwitSerializer(serializers.ModelSerializer):
    user = PublicUserSerializer(read_only=True)

    class Meta:
        model = ReTwit
        fields = ["id", "user", "twit", "created"]
