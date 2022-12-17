from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'account', views.AccountViewSet, basename='account')
router.register(r'comment1', views.CommentViewSet1, basename='comment1')
router.register(r'comment2', views.CommentViewSet2, basename='comment2')
urlpatterns = router.urls

urlpatterns += [
    path('account/create2/', views.AccountCreateView2.as_view(), name='account_create2'),
    path('account/<int:account_id>/', views.AccountView.as_view(), name='account_view'),
    path('account/<int:account_id>/videos/', views.AccountVideoView.as_view(), name='account_video'),
    path('account/<int:account_id>/videos_with_serializer/', views.AccountVideoWithSerializerView.as_view(), name='account_video_with_serializer'),
    path('account/create/', views.AccountCreateView.as_view(), name='account_create'),
]
