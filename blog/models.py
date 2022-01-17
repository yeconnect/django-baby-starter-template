from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100,unique=True,primary_key=True)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey(Category,related_name="blog" ,on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField(Tag,related_name="blog")

    def __str__(self):
        return self.title