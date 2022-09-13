from rest_framework import serializers
from .models import Blog, ThumbUp


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


class ThumbUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThumbUp
        fields = "__all__"
