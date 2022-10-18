from django.urls import include, path
from rest_framework.routers import DefaultRouter

from todo import views

router = DefaultRouter()
router.register('', views.TodoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
