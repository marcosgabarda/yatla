import django_filters

from yatla.twits.models import Twit


class FollowModelFilter(django_filters.rest_framework.FilterSet):

    user = django_filters.CharFilter(field_name="user__pk")

    class Meta:
        model = Twit
        fields = ["user"]
