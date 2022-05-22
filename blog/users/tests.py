from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from blog.users.models import Blogger
from http import HTTPStatus


class TestBloggers(TestCase):
    fixtures = [
        "bloggers.json",
        "users.json",
    ]

    def setUp(self) -> None:
        self.blogger1 = Blogger.objects.get(pk=1)
        self.blogger2 = Blogger.objects.get(pk=2)
        self.blogger3 = Blogger.objects.get(pk=3)

        self.user2 = User.objects.get(pk=2)
        self.user3 = User.objects.get(pk=3)
        self.user4 = User.objects.get(pk=4)

    def test_bloggers_list(self):
        response = self.client.get("/api/v1/users/")
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.data["results"][0]["id"], 1)

    def test_blogger_follow(self):
        client = APIClient()
        data = {"follow": 2}
        response = client.put(
            "/api/v1/users/1",
            data=data,
            format="json",
            follow=True,
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
