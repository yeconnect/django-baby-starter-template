from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('before',views.n_plus_one,name='bad'),
    path('after',views.not_n_plus_one,name='good'),
]