from test_plus import TestCase

from yatla.follows.tests.factories import FollowFactory
from yatla.twits.models import Twit
from yatla.twits.tests.factories import TwitFactory, ReTwitFactory
from yatla.users.tests.factories import UserFactory


class CouponTests(TestCase):
    def setUp(self):
        self.user = self.make_user()

    def test_timeline(self):
        TwitFactory.create_batch(size=1000)
        other_user = UserFactory()
        FollowFactory(user=self.user, follows=other_user)
        twits = TwitFactory.create_batch(size=100, user=other_user)
        ReTwitFactory.create_batch(size=10)
        retwits = ReTwitFactory.create_batch(size=10, user=other_user)
        self.assertEqual(
            len(twits) + len(retwits), Twit.objects.timeline(user=self.user).count()
        )
