from django.http import HttpResponse
from django.urls import path
from .views import todo_all

urlpatterns = [
    path('',todo_all,name="todo_all"),
]