# test for blog/views.py

from django.test import TestCase

from blog.models import Blog
from users.models import CustomUser

from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from django.conf import settings

settings.DEBUG = True


class TestBlogView(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            email="test@gmail.com",
            first_name="test",
            last_name="test",
            password="test",
            is_staff=True,
        )
        self.blog = Blog.objects.create(
            author=self.user,
            title="test",
            body="test",
        )
        self.client = APIClient()

        refresh = RefreshToken.for_user(self.user)
        self.access_token = refresh.access_token

    def test_blog_list(self):
        response = self.client.get("/blog/blog/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["results"][0]["title"], "test")

    def test_blog_detail(self):
        response = self.client.get("/blog/blog/1/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "test")

    def test_blog_create(self):
        request_data = {
            "author": self.user.id,
            "title": "test2",
            "body": "test2",
        }
        response = self.client.post(
            "/blog/blog/",
            request_data,
            HTTP_AUTHORIZATION=f"JWT {self.access_token}")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["title"], "test2")

    def test_blog_update(self):
        request_data = {
            "author": self.user.id,
            "title": "test2",
            "body": "test2",
        }
        response = self.client.put(
            "/blog/blog/1/",
            request_data,
            HTTP_AUTHORIZATION=f"JWT {self.access_token}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "test2")

    def test_blog_delete(self):
        response = self.client.delete(
            "/blog/blog/1/",
            HTTP_AUTHORIZATION=f"JWT {self.access_token}")
        self.assertEqual(response.status_code, 204)
