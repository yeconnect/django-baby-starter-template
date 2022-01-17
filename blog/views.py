from django.http import HttpResponse

from .models import Tag, Category, Blog
from django.db.models import Prefetch

def n_plus_one(request):
    blogs = Blog.objects.all()

    # ここでN+1を起こす
    for blog in blogs:
        print(blog.title)
        print(blog.category.name)

        for category in blog.tag.all():
            print(category.name)

    return HttpResponse("<html><body>ターミナルをチェック！</body></html>")

def not_n_plus_one(request):
    blogs = Blog.objects.all().prefetch_related('tag').select_related('category')

    # ここでN+1を起こす
    for blog in blogs:
        print(blog.title)
        print(blog.category.name)

        for category in blog.tag.all():
            print(category.name)

    return HttpResponse("<body>ターミナルをチェック！</body>")