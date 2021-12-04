from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('bad/',views.bad_increment,name='bad'),
    path('good/',views.good_increment,name='good'),
]