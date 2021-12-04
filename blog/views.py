from django.http.response import HttpResponse
from .models import Article
from django.db.models import F

def bad_increment(request):
  """ シンプルに+1をするとき """
  sample_article = Article.objects.get(title="sampletitle")
  sample_article.access_count += 1 # 一度アクセス数を取ってきて、それに1を加える
  sample_article.save() # それをDBに保存する
  return HttpResponse('+1 finished')

def good_increment(request):
  """ F関数を使った+1 """
  Article.objects.filter(title="sampletitle").update(access_count=F('access_count') + 1) # アクセス数はとって来ず、「アクセス数を1増やせ」とDBに命令する
  return HttpResponse('+1 finished')

