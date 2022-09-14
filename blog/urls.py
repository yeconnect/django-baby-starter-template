from django.urls import path
from .views import BlogViewSet
from rest_framework import viewsets
from rest_framework.routers import DefaultRouter

app_name = "blog"

router = DefaultRouter()
router.register("", BlogViewSet)

urlpatterns = router.urls
