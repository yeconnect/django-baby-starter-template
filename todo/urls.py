from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('',views.wait_a_second,name='wait_a_second'),
]