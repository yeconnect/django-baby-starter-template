from django.contrib import admin
from django.urls import path, include
from django.http.response import HttpResponse
from django.core import management

def create_erd(request):
    management.call_command('graph_models',all_applications=True,pygraphviz=True,output="erd_of_all.png") # ER図を作成、erd.pngとして保存
    with open("./erd_of_all.png", "rb") as f:
        erd_img = f.read()
        return HttpResponse(erd_img, content_type="image/png")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('erd/',create_erd),
    path('blog/',include('blog.urls')),
    path('todo/',include('todo.urls'))
]
