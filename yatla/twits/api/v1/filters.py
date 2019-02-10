import django_filters

from yatla.twits.models import Twit


class TwitModelFilter(django_filters.rest_framework.FilterSet):

    search = django_filters.CharFilter(field_name="field__pk", lookup_expr="icontains")

    class Meta:
        model = Twit
        fields = ["search"]
