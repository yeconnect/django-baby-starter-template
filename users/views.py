from django.contrib.auth import login, logout
from rest_framework import generics, views
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class LoginView(generics.GenericAPIView):
    """ログインAPIクラス"""
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        login(request, user)
        return Response({'message': "ログインが成功しました。", 'access_token': access_token, 'refresh_token': str(refresh)})


class LogoutView(views.APIView):
    """ログアウトAPIクラス"""
    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({'message': "ログアウトが成功しました。"})