from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('',views.sample_func,name='sample'),
]