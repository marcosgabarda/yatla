from django.contrib import admin

from yatla.twits.models import Twit


@admin.register(Twit)
class TwitAdmin(admin.ModelAdmin):
    list_display = ["id", "text", "user", "created"]
