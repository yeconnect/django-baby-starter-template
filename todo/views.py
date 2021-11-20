from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from .models import Todo

def todo_all(request):
  all_todos = Todo.objects.all()
  return HttpResponse(f'<h1>{len(all_todos)}件ありました。</h1><h2>ターミナルにSQLが表示されています。</h2>')

def todo_all_with_query(request):
  print("発行されたSQL",Todo.objects.all().query)
  return HttpResponse(f'.queryを使う方法です。ターミナルにSQLが表示されています。</h2>')
