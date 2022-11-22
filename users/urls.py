from django.urls import path
from .views import LoginView, LogoutView
from rest_framework.routers import DefaultRouter

app_name = "user"

router = DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout")
]