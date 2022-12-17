# serializers.py

from rest_framework import serializers
from .models import Account, Video, Comment


class AccountSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Account.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance)
        instance.save()


class AccountModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username', 'email', 'password']


class VideoSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    video = serializers.FileField()
    thumbnail = serializers.ImageField()
    account = AccountModelSerializer()

    def create(self, validated_data):
        return Video.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.video = validated_data.get('video', instance.video)
        instance.thumbnail = validated_data.get('thumbnail', instance.thumbnail)
        instance.account = validated_data.get('account', instance.account)
        instance.save()


class VideoModelSerializer(serializers.ModelSerializer):
    account = AccountModelSerializer()

    class Meta:
        model = Video
        fields = ['title', 'description', 'video', 'thumbnail', 'account']


class CommentSerializer(serializers.ModelSerializer):
    account = AccountModelSerializer()
    video = VideoModelSerializer()

    class Meta:
        model = Comment
        fields = '__all__'


# 出力
class CommentReadSerializer(serializers.ModelSerializer):
    account = AccountModelSerializer()
    video = VideoModelSerializer()

    class Meta:
        model = Comment
        fields = '__all__'


# 入力
class CommentWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
