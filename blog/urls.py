from django.urls import path
from .views import BlogViewWithoutSerializer, BlogViewWithSerializer, ThumbUpCreateView, BlogCreateView, N_plus_one_View, BlogViewSet, BlogCreateView
from rest_framework.routers import DefaultRouter

app_name = "blog"

router = DefaultRouter()
router.register(r'thumb_up_create', ThumbUpCreateView, basename='thumb_up_create')
router.register(r'n_plus_one', N_plus_one_View, basename='n_plus_one')
router.register(r'blog', BlogViewSet, basename='blog')
router.register(r'blog_create', BlogCreateView, basename='blog_create')

urlpatterns = router.urls

urlpatterns += [
    path("without_serializer/", BlogViewWithoutSerializer.as_view(), name="without_serializer"),
    path("with_serializer/", BlogViewWithSerializer.as_view(), name="with_serializer")
]
