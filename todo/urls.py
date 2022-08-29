from django.urls import path
from django.http import HttpResponse
from .views import delete_todo, post_todo, todo_func, get_todo_list, put_todo, get_todo

# use views.py
urlpatterns = [
    path("", todo_func),
    path("<int:id>", get_todo),
    path("list", get_todo_list),
    path("create", post_todo),
    path("update/<int:id>", put_todo),
    path("delete/<int:id>", delete_todo),
]
