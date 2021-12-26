from django.db import models

class ToitterUser(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    # ↓ここ！
    following = models.ManyToManyField("self",related_name="followed_by",symmetrical=False,blank=True)

    def __str__(self):
        return self.username