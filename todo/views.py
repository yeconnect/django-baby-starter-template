from unittest import result

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Todo


@csrf_exempt
def sample(request):
    if request.method == "GET":
        todos = Todo.objects.all()
        result = "Todos in DB →"
        for todo in todos:
            result += todo.title
        return HttpResponse(result)
    if request.method == "POST":
        new_todo = Todo(title="hogehoge", content="fasdfas")
        new_todo.save()
        return HttpResponse('new todo saved')
