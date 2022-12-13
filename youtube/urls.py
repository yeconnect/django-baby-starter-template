from django.urls import path
from . import views

app_name = 'youtube'

urlpatterns = [
    path('account/<int:account_id>/videos/', views.AccountVideoView.as_view(), name='account_video'),
]