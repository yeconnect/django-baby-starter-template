from django.http.response import HttpResponse
from django.core import management
from .models import BlogUser

def create_erd(request):
    management.call_command('graph_models','blog',pygraphviz=True,output="erd_of_blog.png") # ER図を作成、erd.pngとして保存
    with open("./erd_of_blog.png", "rb") as f:
        erd_img = f.read()
        return HttpResponse(erd_img, content_type="image/png")

def follow(request,id):
    user = BlogUser.objects.get(id=id)
    followings =user.following.all()
    followins_str = ','.join([user.name for user in followings])
    followed_bys = user.followed_by.all()
    followed_bys_str = ','.join([user.name for user in followed_bys])

    html = f"""
    <div>
        <h2>ID:{id}がフォローしている人</h2>
        {followins_str}
        <h2>ID:{id}のフォロワー</h2>
        {followed_bys_str}
    </div>
    """

    return HttpResponse(html)

def fl(request):
    user1 = BlogUser.objects.get(id=1)
    user2 = BlogUser.objects.get(id=2)

    user2.followed_by.add(user1)
    return HttpResponse('good')


