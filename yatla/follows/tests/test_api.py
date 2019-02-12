from test_plus import APITestCase

from yatla.users.tests.factories import UserFactory


class FollowsAPITestCase(APITestCase):
    user_factory = UserFactory

    def setUp(self):
        self.user = self.make_user()

    def test_start_follow(self):
        user = UserFactory()
        with self.login(self.user):
            data = {
                "follows": user.username
            }
            self.post("/api/v1/follows/", data=data)
            print(self.last_response.json())
            self.response_201()
