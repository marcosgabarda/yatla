import django_filters

from yatla.follows.models import Follow


class FollowModelFilter(django_filters.rest_framework.FilterSet):

    user = django_filters.CharFilter(field_name="user__pk")

    class Meta:
        model = Follow
        fields = ["user"]
