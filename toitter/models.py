from django.db import models

# Create your models here.
class ToitterUser(models.Model):
    username = models.CharField(max_length=30)
    following = models.ManyToManyField("self",related_name="followed_by",symmetrical=False,blank=True)

    def __str__(self):
        return self.name