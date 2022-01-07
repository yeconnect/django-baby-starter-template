from django.http.response import HttpResponse

def sample_func(request):
    print('ここがviews.py、sample_funcなう')
    return HttpResponse('Hello World from todo app')