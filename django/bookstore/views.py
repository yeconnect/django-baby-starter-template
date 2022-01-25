import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt 
def handle_message(request):

    if request.method == "GET":
        return JsonResponse({"message":"こんばんは！！"})

    if request.method == "POST":
        print(request.POST)
        return JsonResponse({"message":"データを受け取りました"})