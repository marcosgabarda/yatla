from rest_framework import serializers

from yatla.twits.models import Twit
from yatla.users.api.v1.serializers import PublicUserSerializer


class TwitSerializer(serializers.ModelSerializer):
    user = PublicUserSerializer(read_only=True)

    class Meta:
        model = Twit
        fields = ["id", "user", "text", "likes", "retwits", "created"]
