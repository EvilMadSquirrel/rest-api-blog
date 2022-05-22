from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from blog.users.models import Blogger
from blog.posts.models import Post
from http import HTTPStatus


class TestPosts(TestCase):
    fixtures = ['bloggers.json', 'users.json', 'posts.json']

    def setUp(self) -> None:
        self.blogger1 = Blogger.objects.get(pk=1)
        self.blogger2 = Blogger.objects.get(pk=2)
        self.blogger3 = Blogger.objects.get(pk=3)

        self.user2 = User.objects.get(pk=2)
        self.user3 = User.objects.get(pk=3)
        self.user4 = User.objects.get(pk=4)

        self.post1 = Post.objects.get(pk=1)
        self.post2 = Post.objects.get(pk=2)
        self.post3 = Post.objects.get(pk=3)
        self.post4 = Post.objects.get(pk=4)
        self.post5 = Post.objects.get(pk=5)
        self.post6 = Post.objects.get(pk=6)
        self.post7 = Post.objects.get(pk=7)
        self.post8 = Post.objects.get(pk=8)
        self.post9 = Post.objects.get(pk=9)
        self.post10 = Post.objects.get(pk=10)
        self.post11 = Post.objects.get(pk=11)
        self.post13 = Post.objects.get(pk=13)
        self.post14 = Post.objects.get(pk=14)
        self.post15 = Post.objects.get(pk=15)

    def test_user_news(self):
        client = APIClient()
        response = client.get('/api/v1/users/3/news/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(response.data['results']), 10)

    def test_user_posts(self):
        client = APIClient()
        response = client.get('/api/v1/users/3/posts/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(response.data['results']), 4)

    def test_read_post(self):
        client = APIClient()
        data = {
            'readers': 3
        }
        response = client.put('/api/v1/users/3/news/5', data=data, format='json', follow=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)
