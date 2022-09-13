from django.db import models
from users.models import CustomUser


class Blog(models.Model):
    author = models.ForeignKey(CustomUser, related_name="blogs", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ThumbUp(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, related_name="thumb_ups", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog.title


class Tag(models.Model):
    name = models.CharField(max_length=200)
    blogs = models.ManyToManyField(Blog, related_name="tags")

    def __str__(self):
        return self.name
