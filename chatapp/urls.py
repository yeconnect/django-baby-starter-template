from django.urls import path
from django.http.response import HttpResponse
from . import views

app_name = 'chatapp'

def chatapp_like_func(request):
    # chatappにいいねをする機能
    return HttpResponse('いいねしました')

urlpatterns = [
    path('like', chatapp_like_func),
]
