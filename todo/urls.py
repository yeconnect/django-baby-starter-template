from django.urls import path

from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.sample, name='func'),
    path('api', views.api, name='api')
]
