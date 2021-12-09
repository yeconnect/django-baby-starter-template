from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('',views.fl,name='fl'),
    path('erd',views.create_erd,name='create_erd'),
    path('follow/<int:id>',views.follow,name='foloow'),
]