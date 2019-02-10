from factory import DjangoModelFactory, SubFactory
from factory.fuzzy import FuzzyText

from yatla.twits.models import Twit, ReTwit, Like
from yatla.users.tests.factories import UserFactory


class TwitFactory(DjangoModelFactory):
    user = SubFactory(UserFactory)
    text = FuzzyText(length=280)

    class Meta:
        model = Twit


class LikeFactory(DjangoModelFactory):
    user = SubFactory(UserFactory)
    twit = SubFactory(TwitFactory)

    class Meta:
        model = Like


class ReTwitFactory(DjangoModelFactory):
    user = SubFactory(UserFactory)
    twit = SubFactory(TwitFactory)

    class Meta:
        model = ReTwit
