from django.conf import settings
from django.db import models
from model_utils.models import TimeStampedModel

from yatla.twits.managers import TwitQuerySet


class Twit(TimeStampedModel):
    """Twit message from a user."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="twits", on_delete=models.CASCADE
    )
    text = models.CharField(max_length=280)

    objects = TwitQuerySet.as_manager()

    class Meta:
        ordering = ["-created"]

    @property
    def likes(self):
        """Number of likes."""
        return self.liked_by.count()

    @property
    def retwits(self):
        """Number of retwits."""
        return self.retwitted_by.count()


class Like(TimeStampedModel):
    """A user likes a twit."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="likes", on_delete=models.CASCADE
    )
    twit = models.ForeignKey(
        "twits.Twit", related_name="liked_by", on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ["user", "twit"]


class ReTwit(TimeStampedModel):
    """A user retwits a twit."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="retwits", on_delete=models.CASCADE
    )
    twit = models.ForeignKey(
        "twits.Twit", related_name="retwitted_by", on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ["user", "twit"]
