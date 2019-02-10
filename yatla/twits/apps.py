from django.apps import AppConfig


class TwitsAppConfig(AppConfig):

    name = "yatla.twits"
    verbose_name = "Twits"

    def ready(self):
        try:
            pass
        except ImportError:
            pass
