from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .filters import TodoFilter
from .models import Todo
from .serializers import (CommentSerializer, TekitouListGenerateSerializer,
                          TodoSerializer)

"""
viewsets.ModelViewSetの定義を見ると
https://github.com/encode/django-rest-framework/blob/35c5be6ec23af6e68914812599c905fe0fa2c0cc/rest_framework/viewsets.py#L239-L244

class ModelViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
となっているから、必要ないHTTPメソッドは省ける。
"""

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filterset_class = TodoFilter

    """
    """
    def get_serializer_class(self):
        # actionによってserializerを変えることで、drf-spectacularに使うserializerを伝えることができ、自動生成がうまくいく。
        if self.action == 'list':
            return TodoSerializer
        elif self.action == 'retrieve':
            return TodoSerializer
        elif self.action == 'create':
            return TodoSerializer
        elif self.action == 'update':
            return TodoSerializer
        elif self.action == 'partial_update':
            return TodoSerializer

    @extend_schema(responses={200: TodoSerializer(many=True)}, description="完了済みのTODOを取得する")
    @action(detail=False, methods=['get'])
    def completed(self, request):
        queryset = self.get_queryset().filter(completed=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @extend_schema(request=CommentSerializer , responses={204: None}, description="{pk}番目のTODOにコメントを追加する")
    @action(detail=True, methods=['post'])
    def comment(self, request, pk=None):
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print('このコメントデータを保存するなど', serializer.validated_data)
        return Response(status=204)

    @extend_schema(responses={200: TekitouListGenerateSerializer()}, description="{pk}番目のTODOの各カラムを空配列に足していくものを返す")
    @action(detail=True, methods=['get'])
    def tekitou_list_generate(self, request, pk=None):
        todo = self.get_object()
        serializer = TekitouListGenerateSerializer(todo)
        return Response(serializer.data)

@extend_schema_view(
    completed=extend_schema(responses={200: TodoSerializer(many=True)}, description="完了済みのTODOを取得する"),
    comment=extend_schema(request=CommentSerializer , responses={204: None}, description="{pk}番目のTODOにコメントを追加する"),
    tekitou_list_generate=extend_schema(responses={200: TekitouListGenerateSerializer()}, description="{pk}番目のTODOの各カラムを空配列に足していくものを返す"),
)
class TodoViewSetEqual(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filterset_class = TodoFilter

    @action(detail=False, methods=['get'])
    def completed(self, request):
        queryset = self.get_queryset().filter(completed=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def comment(self, request, pk=None):
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print('このコメントデータを保存するなど', serializer.validated_data)
        return Response(status=204)

    @action(detail=True, methods=['get'])
    def tekitou_list_generate(self, request, pk=None):
        todo = self.get_object()
        serializer = TekitouListGenerateSerializer(todo)
        return Response(serializer.data)


# APIViewにスキーマヒントを与えられるか検証
@extend_schema_view(
    get=extend_schema(responses={200: TodoSerializer(many=True)}, description="TODOを全件取得する"),
)
class TestShema(APIView):
    def get(self, request, format=None):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
