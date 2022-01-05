from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

app_name = 'blog'
urlpatterns = [
    path('bad/',views.bad_increment,name='bad'),
    path('good/',views.good_increment,name='good'),
    path('cache/',views.cache_func_test,name='cache'),
    path('cache_delete/',views.delete_cache,name='delete_cache'),
]