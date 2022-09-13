from rest_framework.views import APIView
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.response import Response


class BlogListView(APIView):
    def get(self, request, format=None):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BlogSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class BlogDetailView(APIView):
    def get(self, request, pk, format=None):
        blog = Blog.objects.get(id=pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        blog = Blog.objects.get(id=pk)
        serializer = BlogSerializer(blog, data=request.data)
        serializer.is_valid(raise_expception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        blog = Blog.objects.get(id=pk)
        blog.delete()
        return Response("Blog deleted")
