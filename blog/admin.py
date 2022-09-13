from django.contrib import admin
from .models import Blog, ThumbUp, Tag

admin.site.register(Blog)
admin.site.register(ThumbUp)
admin.site.register(Tag)
