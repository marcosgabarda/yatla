from django.db import models
from django.db.models import Q


class TwitQuerySet(models.QuerySet):
    def timeline(self, user):
        """Gets the twits of the timeline from the given user."""
        following_pks = user.following.values_list("follows__pk", flat=True)
        return self.filter(
            Q(user__pk__in=following_pks) | Q(retwitted_by__user__pk__in=following_pks)
        )
