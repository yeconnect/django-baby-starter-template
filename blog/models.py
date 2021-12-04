from django.db import models

class Article(models.Model):
  title = models.CharField(max_length=50, unique=True)
  content = models.TextField(null=True,blank=True)
  access_count = models.PositiveBigIntegerField(default=0)

  def __str__(self):
    return self.title