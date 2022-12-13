from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Account, Video


#あるAccountが出したVideo一覧
class AccountVideoView(APIView):
    def get(self, request, account_id):
        videos = Video.objects.filter(account_id=account_id)
        res_videos = []
        for video in videos:
            res_video = {
                'id': video.id,
                'title': video.title,
                'description': video.description,
                'video': video.video.url,
                'thumbnail': video.thumbnail.url,
                'created_at': video.created_at,
                'updated_at': video.updated_at,
                'account': video.account.username,
                'comment_accounts': video.comment_accounts.all().values('username'),
                'like_accounts': video.like_accounts.all().values('username'),
            }
            res_videos.append(res_video)
        return Response(res_videos)