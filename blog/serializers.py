from rest_framework import serializers
from .models import Blog, ThumbUp
from users.models import CustomUser
from drf_spectacular.utils import extend_schema_field, OpenApiTypes


class BlogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField(write_only=True)
    author_name = serializers.SerializerMethodField(read_only=True)
    title = serializers.CharField()
    body = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Blog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if validated_data.get("author"):
            instance.author = CustomUser.objects.get(id=validated_data["author"])
        instance.title = validated_data.get("title", instance.title)
        instance.body = validated_data.get("body", instance.body)
        instance.save()
        return instance
    
    def get_author_name(self, obj):
        return obj.author.first_name + "さん"

    class Meta:
        model = Blog
        fields = "__all__"


class BlogModelSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField(read_only=True)

    @extend_schema_field(OpenApiTypes.STR)
    def get_author_name(self, obj):
        return obj.author.first_name + "さん"

    class Meta:
        model = Blog
        fields = "__all__"


class ThumbUpReadSerializer(serializers.ModelSerializer):
    blog = BlogSerializer()
    class Meta:
        model = ThumbUp
        fields = "__all__"


class ThumbUpWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = ThumbUp
        fields = "__all__"
