from django.urls import path
from . import views

app_name = 'bookstore'

urlpatterns = [
    path('message',views.handle_message,name='func'),
]