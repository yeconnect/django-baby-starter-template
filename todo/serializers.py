from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

class CommentSerializer(serializers.Serializer):
    comment = serializers.CharField()
    email = serializers.EmailField()


class TekitouListGenerateSerializer(serializers.Serializer):
    
    tekitou_list = serializers.SerializerMethodField()

    @extend_schema_field(serializers.ListField(child=serializers.CharField()))
    def get_tekitou_list(self, obj):
        tekitou_list = [obj.title, obj.description, obj.comment]
        return tekitou_list
