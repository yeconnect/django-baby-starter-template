from django.urls import path
from . import views

app_name = 'toitter'
urlpatterns = [
    path('',views.top,name='top'),
    path('<str:username>/followees', views.followees_func, name="followees"),
    path('<str:username>/followers', views.followers_func, name="followers"),
    #path('<username:str>/follow/<target_username:str>', views.followees_func, name="followees"),
]