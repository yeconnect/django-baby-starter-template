from django.urls import path
from . import views

app_name = 'toitter'
urlpatterns = [
    path('',views.fl,name='list'),
]