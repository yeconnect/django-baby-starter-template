from django.http.response import HttpResponse
from django.urls import path
from django.urls.conf import include

def sample_func(request):
    print('sample_funcなう')
    return HttpResponse('Hello World')

urlpatterns = [
    path('todo/', include('todo.urls')),
]
