from django.db import models
from blog.models import BlogUser

class Todo(models.Model):
    author = models.ForeignKey(BlogUser,models.CASCADE)
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class CommentToTodo(models.Model):
    todo = models.ForeignKey(Todo,models.CASCADE)
    author = models.ForeignKey(BlogUser,models.CASCADE)
    content = models.TextField()