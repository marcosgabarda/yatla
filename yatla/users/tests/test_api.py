from rest_framework import status
from rest_framework.test import APITestCase

from yatla.users.models import User
from yatla.users.tests.factories import UserFactory


class UserAPITests(APITestCase):
    def setUp(self):
        self.user = UserFactory()

    def test_list_users(self):
        UserFactory.create_batch(size=10)
        self.client.force_authenticate(self.user)
        response = self.client.get("/api/v1/users/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(1, data["count"])

    def test_register_user(self):
        users = User.objects.all().count()
        data = {"username": "new", "email": "new@example.com", "password": "secure"}
        response = self.client.post("/api/v1/users/", data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(users + 1, User.objects.all().count())
        user = User.objects.get(email=data["email"])
        self.assertTrue(user.check_password(data["password"]))

    def test_get_me(self):
        self.client.force_authenticate(self.user)
        response = self.client.get("/api/v1/users/me/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertIn("id", data)

    def test_update_me(self):
        self.client.force_authenticate(self.user)
        data = {
            "username": "client1",
            "email": "client1@example.com",
            "password": "new_password",
        }
        response = self.client.patch("/api/v1/users/me/", data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user = User.objects.get(pk=self.user.pk)
        self.assertEqual(data["email"], user.email)
        self.assertTrue(user.check_password(data["password"]))
