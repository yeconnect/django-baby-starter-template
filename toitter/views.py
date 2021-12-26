from django.shortcuts import get_object_or_404, render
from .models import ToitterUser

def top(request):
    all_users = ToitterUser.objects.all()

    context = { "all_users":all_users }

    return render(request,"top.html",context)

def followees_func(request,username):
    user = get_object_or_404(ToitterUser,username=username)

    followees = user.following.all()
    print(followees) # ちゃんとフォロワーが全員取れていることをチェック

    context = {"user": user, "followees":followees}

    return render(request,"followees.html",context)

def followers_func(request,username):
    user = get_object_or_404(ToitterUser,username=username)

    followers = user.followed_by.all()
    print(followers) # ちゃんとフォロワーが全員取れていることをチェック

    context = {"user": user, "followers":followers}

    return render(request,"followers.html",context)