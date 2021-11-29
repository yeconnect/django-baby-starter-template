from django.http import HttpResponse
from django.urls import path
from .views import todo_all, todo_all_with_query, transaction_view, without_transaction

urlpatterns = [
    path('',todo_all,name="todo_all"),
    path('query',todo_all_with_query,name="query"),
    path('without_transaction',without_transaction,name="withou-transaction"),
    path('with_transaction',transaction_view,name="transaction"),
]