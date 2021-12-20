from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('erd',views.create_erd,name='erd'),
]