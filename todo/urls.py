from django.http import HttpResponse
from django.urls import path
from .views import todo_all, todo_all_with_query

urlpatterns = [
    path('',todo_all,name="todo_all"),
    path('query',todo_all_with_query,name="query"),
]