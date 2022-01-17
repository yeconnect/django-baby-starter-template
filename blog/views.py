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

    return HttpResponse("ターミナルをチェック！")

def not_n_plus_one(request):
    blogs = Blog.objects.all().select_related('category').prefetch_related('tag')

    # ここでN+1を起こす
    for blog in blogs:
        print(blog.title)
        print(blog.category.name)

        for category in blog.tag.all():
            print(category.name)

    return HttpResponse("ターミナルをチェック！")