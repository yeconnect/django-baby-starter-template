from rest_framework.decorators import action
from .models import Blog
from .serializers import BlogSerializer, BlogSerializer2
from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import get_object_or_404


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def retrieve(self, request, pk=None):
        queryset = Blog.objects.all()
        blog = get_object_or_404(queryset, pk=pk)
        serializer = BlogSerializer2(blog)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def get_blog_list_custom(self, request):
        blog = Blog.objects.all()
        serializer = BlogSerializer(blog, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["put"])
    def put_blog_custom(self, request, pk):
        blog = Blog.objects.get(id=pk)
        serializer = BlogSerializer(blog, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
