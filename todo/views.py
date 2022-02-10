from unittest import result

import requests
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


def api(request):
    sample_url = "https://api.apollon.ai/"
    try:
        res = requests.get(sample_url, timeout=(3.0, 6.0))
        return HttpResponse(res)
    except Exception as e:
        print(str(e))
        return HttpResponse('error')
