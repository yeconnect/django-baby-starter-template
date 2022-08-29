import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Todo

# Create your views here.


def todo_func(request):
    return HttpResponse("todo world")


def get_todo_list(request):
    todo_list = Todo.objects.all().values()
    return HttpResponse(todo_list)


def get_todo(request, id):
    if request.method == "GET":
        todo = Todo.objects.filter(id=id).values()
        return HttpResponse(todo)
    else:
        return HttpResponse("fail")


@csrf_exempt
# create Todo
def post_todo(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(request.POST.get("title",None))
        title = data.get("title")
        description = data.get("description")
        Todo.objects.create(title=title, description=description)
        return HttpResponse("success")
    else:
        return HttpResponse("fail")


# update Todo
def put_todo(request, id):
    if request.method == "PUT":
        title = request.POST.get("title")
        description = request.POST.get("description")
        completed = request.POST.get("completed")
        created_at = request.POST.get("created_at")
        updated_at = request.POST.get("updated_at")
        Todo.objects.filter(id=id).update(
            title=title, description=description, completed=completed, created_at=created_at, updated_at=updated_at
        )
        return HttpResponse("success")
    else:
        return HttpResponse("fail")


# delete Todo
def delete_todo(request, id):
    if request.method == "DELETE":
        Todo.objects.filter(id=id).delete()
        return HttpResponse("success")
    else:
        return HttpResponse("fail")
