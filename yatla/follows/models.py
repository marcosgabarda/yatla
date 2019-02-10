from django.conf import settings
from django.db import models
from model_utils.models import TimeStampedModel


class Follow(TimeStampedModel):
    """The user follows an other user."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="following", on_delete=models.CASCADE
    )
    follows = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="followers", on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ["user", "follows"]
