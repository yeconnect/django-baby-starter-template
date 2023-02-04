from django.urls import path
from django.http.response import HttpResponse
from . import views

app_name = 'chatapp'

def chatapp_like_func(request):
    # chatappにいいねをする機能
    return HttpResponse('いいねしました')

urlpatterns = [
    path('like', chatapp_like_func),
    path('get_user/<int:user_id>', views.get_user),
    path('get_message', views.get_message),
    path('get_messages_of_user/<int:user_id>', views.get_messages_of_user),
]
