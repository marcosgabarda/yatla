import django_filters

from yatla.twits.models import Twit, Like, ReTwit


class TwitModelFilter(django_filters.rest_framework.FilterSet):

    search = django_filters.CharFilter(field_name="text", lookup_expr="icontains")

    class Meta:
        model = Twit
        fields = ["search"]


class LikeModelFilter(django_filters.rest_framework.FilterSet):

    user = django_filters.NumberFilter(field_name="user__pk")
    twit = django_filters.NumberFilter(field_name="twit__pk")

    class Meta:
        model = Like
        fields = ["twit", "user"]


class ReTwitModelFilter(django_filters.rest_framework.FilterSet):

    user = django_filters.NumberFilter(field_name="user__pk")
    twit = django_filters.NumberFilter(field_name="twit__pk")

    class Meta:
        model = ReTwit
        fields = ["twit", "user"]
