import json
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import ChatappUser

# Create your views here.

def get_user(request, user_id):
    user = ChatappUser.objects.get(id=user_id)
    # slect * from user where id = user_id
    data = {
        'name': user.name,
        'image': user.image,
        'id':user_id,
    }
    return JsonResponse(data)