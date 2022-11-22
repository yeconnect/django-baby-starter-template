from blog.serializers import BlogModelSerializer
from django.test import TestCase
from blog.models import Blog
from users.models import CustomUser


class TestBlogModelSerializer(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            email="test@gmail.com",
            first_name="test",
            last_name="test",
            password="test",
        )
        self.blog = Blog.objects.create(
            author=self.user,
            title="test",
            body="test",
        )
        self.serializer = BlogModelSerializer

    def test_valid_data(self):
        request_data = {
            "author": self.user.id,
            "title": "test",
            "body": "test",
        }
        validated_data = {
            "author": self.user,
            "title": "test",
            "body": "test",
        }
        serializer = self.serializer(data=request_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(dict(serializer.validated_data), validated_data)
