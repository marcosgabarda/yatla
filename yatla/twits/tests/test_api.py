from test_plus import APITestCase

from yatla.follows.tests.factories import FollowFactory
from yatla.twits.models import Twit
from yatla.twits.tests.factories import TwitFactory, ReTwitFactory
from yatla.users.tests.factories import UserFactory


class TwitAPITestCase(APITestCase):
    user_factory = UserFactory

    def setUp(self):
        self.user = self.make_user()

    def test_list_twits(self):
        twits = TwitFactory.create_batch(size=1000)
        self.get("/api/v1/twits/")
        self.response_200()
        data = self.last_response.json()
        self.assertEqual(len(twits), data["count"])

    def test_list_timeline(self):
        TwitFactory.create_batch(size=1000)
        other_user = UserFactory()
        FollowFactory(user=self.user, follows=other_user)
        twits = TwitFactory.create_batch(size=100, user=other_user)
        ReTwitFactory.create_batch(size=10)
        retwits = ReTwitFactory.create_batch(size=10, user=other_user)
        with self.login(self.user):
            self.get("/api/v1/twits/timeline/")
            self.response_200()
            data = self.last_response.json()
            self.assertEqual(len(twits) + len(retwits), data["count"])

    def test_create_twit(self):
        with self.login(self.user):
            data = {"text": "New twit!"}
            self.post("/api/v1/twits/", data=data)
            self.response_201()
            self.assertEqual(1, Twit.objects.filter(user=self.user).count())
