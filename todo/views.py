from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from .models import Todo

def todo_all(request):
  all_todos = Todo.objects.all()
  return HttpResponse(f'<h1>{len(all_todos)}件ありました。</h1>')
