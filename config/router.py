from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from yatla.follows.api.v1.viewsets import FollowViewSet
from yatla.twits.api.v1.viewsets import TwitViewSet, LikeViewSet, ReTwitViewSet
from yatla.users.api.v1.viewsets import (
    UserViewSet,
    me
)

app_name = 'api_v1'

router = routers.DefaultRouter()
router.register('users', viewset=UserViewSet)
router.register('twits', viewset=TwitViewSet)
router.register('follows', viewset=FollowViewSet)
router.register('likes', viewset=LikeViewSet)
router.register('re_twits', viewset=ReTwitViewSet)

urlpatterns = [
    path('users/me/', me, kwargs={'pk': 'me'}),
    path('', include(router.urls)),
]
