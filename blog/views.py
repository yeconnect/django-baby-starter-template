import time

from django.http.response import HttpResponse
from django.core.cache import cache

from .models import Article

def cache_func_test(request):

  article = cache.get("article")
  if article:
    print('cache fit')
  else:
    print('cache not hit')
    article = Article.objects.get(title="sample")
    cache.set("article", article)

  return HttpResponse(article.title)

def delete_cache(request):
  cache.set("article", None)
  return HttpResponse('wow')