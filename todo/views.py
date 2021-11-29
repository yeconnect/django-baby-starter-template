from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from .models import Todo
from django.db import transaction

def todo_all(request):
  all_todos = Todo.objects.all()
  return HttpResponse(f'<h1>{len(all_todos)}件ありました。</h1><h2>ターミナルにSQLが表示されています。</h2>')

def todo_all_with_query(request):
  print("発行されたSQL",Todo.objects.all().query)
  return HttpResponse(f'.queryを使う方法です。ターミナルにSQLが表示されています。</h2>')

def without_transaction(request):
  print('トランザクションなし')
  Todo.objects.create(title="トランザクションなしの場合",content="これは残る")
  raise Exception('わざとエラーを生じさせる')
  return HttpResponse('Good')

def transaction_view(request):
  print("トランザクションあり")
  with transaction.atomic():
    Todo.objects.create(title="トランザクションありの場合",content="これは残らない")
    raise Exception('わざとエラーを生じさせる')
  return HttpResponse('Good')