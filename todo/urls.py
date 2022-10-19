from django.urls import include, path
from rest_framework.routers import DefaultRouter

from todo import views

router = DefaultRouter()
router.register('', views.TodoViewSet)
router.register('equal', views.TodoViewSetEqual)

urlpatterns = [
    path('', include(router.urls)),
    path('apiview_test', views.TestShema.as_view())
]
