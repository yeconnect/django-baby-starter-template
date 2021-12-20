from django.http.response import HttpResponse
from django.http.response import HttpResponse
from django.core import management

def create_erd(request):
    management.call_command('graph_models','todo',pygraphviz=True,output="erd_of_todo.png") # ER図を作成、erd.pngとして保存
    with open("./erd_of_todo.png", "rb") as f:
        erd_img = f.read()
        return HttpResponse(erd_img, content_type="image/png")