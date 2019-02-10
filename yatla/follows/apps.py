from django.apps import AppConfig


class FollowsAppConfig(AppConfig):

    name = "yatla.follows"
    verbose_name = "Follows"

    def ready(self):
        try:
            pass
        except ImportError:
            pass
