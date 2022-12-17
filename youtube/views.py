from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Account, Video, Comment
from .serializers import AccountModelSerializer, VideoModelSerializer, CommentSerializer, CommentReadSerializer, CommentWriteSerializer, AccountSerializer, VideoSerializer
from rest_framework import status


# あるAccountが出したVideo一覧
class AccountVideoView(APIView):
    def get(self, request, account_id):
        videos = Video.objects.filter(account_id=account_id)
        res_videos = []
        for video in videos:
            res_video = {
                'title': video.title,
                'description': video.description,
                'video': video.video.url,
                'thumbnail': video.thumbnail.url,
                'account': video.account.id,
            }
            res_videos.append(res_video)
        return Response(res_videos, status=status.HTTP_200_OK)


class AccountVideoWithSerializerView(APIView):
    def get(self, request, account_id):
        videos = Video.objects.filter(account_id=account_id)
        serializer = VideoModelSerializer(videos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AccountView(APIView):
    def get(self, request, account_id):
        account = Account.objects.get(id=account_id)
        res_account = {
            'username': account.username,
            'email': account.email,
            'created_at': account.created_at,
            'updated_at': account.updated_at
        }
        return Response(res_account, status=status.HTTP_200_OK)


class AccountCreateView2(APIView):
    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            "message": "Account created successfully",
            "account": serializer.data
        }
        return Response(response, status=status.HTTP_201_CREATED)


class AccountCreateView(APIView):
    def post(self, request):
        serializer = AccountModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            "message": "Account created successfully",
            "account": serializer.data
        }
        return Response(response, status=status.HTTP_201_CREATED)


class AccountViewSet(ModelViewSet):
    serializer_class = AccountModelSerializer
    queryset = Account.objects.all()


class CommentViewSet1(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentViewSet2(ModelViewSet):
    serializer_class = CommentReadSerializer
    queryset = Comment.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return CommentReadSerializer
        else:
            return CommentWriteSerializer
