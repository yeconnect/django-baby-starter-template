from rest_framework.decorators import action
from .models import Blog, ThumbUp
from users.models import CustomUser
from .serializers import BlogSerializer, ThumbUpReadSerializer, ThumbUpWriteSerializer, BlogModelSerializer
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .pagination import StandardResultsSetPagination
from django.db.models import Prefetch
from users.permissions import IsAdminOrReadOnly, IsAdminOrStaffOrReadOnly
from drf_spectacular.utils import extend_schema
from rest_framework import permissions


class BlogViewWithoutSerializer(APIView):
    def get(self, request, format=None):
        blogs = Blog.objects.all()
        blog_dicts = []
        for blog in blogs:
            blog_dict = {
                "id": blog.id,
                "author": blog.author.id,
                "title": blog.title,
                "body": blog.body,
                "created_at": blog.created_at,
                "updated_at": blog.updated_at,
            }
            blog_dicts.append(blog_dict)
        return Response(blog_dicts, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        if request.data.get("title") is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)        
        if request.data.get("body") is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)        
        if request.data.get("author") is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
 
        Blog.objects.create(
            title=request.data["title"],
            body=request.data["body"],
            author=CustomUser.objects.get(id=request.data["author"]),
        )

        return Response(status=status.HTTP_201_CREATED)


class BlogViewWithSerializer(APIView):
    permission_classes = [IsAdminOrReadOnly, permissions.IsAuthenticated]

    def get(self, request, format=None):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BlogSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def put(self, request, pk, format=None):
        blog = get_object_or_404(Blog, pk=pk)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        blog = get_object_or_404(Blog, pk=pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ThumbUpCreateView(viewsets.ViewSet):
    @action(detail=False, methods=["post"])
    def create_100(self, request):
        for i in range(100):
            user = CustomUser.objects.get(id=1)
            blog = Blog.objects.get(id=1)
            ThumbUp.objects.create(user=user, blog=blog)
        return Response(status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["post"])
    def bulk_create_100(self, request):
        thumb_up_objects = []
        for i in range(100):
            user = CustomUser.objects.get(id=1)
            blog = Blog.objects.get(id=1)
            thumb_up_objects.append(ThumbUp(user=user, blog=blog))
        ThumbUp.objects.bulk_create(thumb_up_objects)
        return Response(status=status.HTTP_201_CREATED)


class BlogCreateView(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    @extend_schema(request=BlogModelSerializer)
    def bulk_create(self, request):
        blog_objects = []
        for _ in range(100):
            author = CustomUser.objects.get(id=1)
            title = "Dummy Title"
            body = "Dummy Body"
            blog_objects.append(
                Blog(author=author, title=title, body=body)
            )
        Blog.objects.bulk_create(blog_objects)
        return Response(status=status.HTTP_201_CREATED)


class N_plus_one_View(viewsets.ViewSet):
    @action(detail=False, methods=["get"])
    def to_one_without_select_related(self, request):
        thumbs = ThumbUp.objects.all()
        serializer = ThumbUpReadSerializer(thumbs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def to_multiple_without_prefetch_related(self, request):
        blog = Blog.objects.get(id=1)
        thumbs = blog.thumb_ups.all()
        for thumb in thumbs:
            print(thumb.user.first_name)
        serializer = ThumbUpReadSerializer(thumbs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def to_one_with_select_related(self, request):
        thumbs = ThumbUp.objects.select_related("blog").select_related("blog__author").all()
        serializer = ThumbUpReadSerializer(thumbs, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=["get"])
    def to_multiple_with_prefetch_related(self, request):
        blog = Blog.objects.prefetch_related(
            Prefetch(
                "thumb_ups",
                queryset=(
                    ThumbUp.objects.select_related("user")
                )
            )
        ).get(id=1)
        thumbs = blog.thumb_ups.all()
        for thumb in thumbs:
            print(thumb.user.first_name)
        serializer = ThumbUpReadSerializer(thumbs, many=True)
        return Response(serializer.data)


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogModelSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAdminOrStaffOrReadOnly]

    @extend_schema(request=BlogModelSerializer, description="HOGEHOGE")
    @action(detail=False, methods=["get"])
    def hoge(self, request):
        serializer = BlogModelSerializer(data=request.data)
        serializer.is_valid()
        return Response(status=status.HTTP_200_OK)
