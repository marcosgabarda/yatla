from factory import DjangoModelFactory, SubFactory

from yatla.follows.models import Follow
from yatla.users.tests.factories import UserFactory


class FollowFactory(DjangoModelFactory):
    user = SubFactory(UserFactory)
    follows = SubFactory(UserFactory)

    class Meta:
        model = Follow
