from django.urls import path
from . import views

app_name = 'chatapp'

urlpatterns = [
    path('room/<int:user_id>/', views.RoomListView.as_view(), name='room_list'),
    path('message/<int:room_id>/', views.MessageListView.as_view(), name='message_list'),
    path('message/<int:room_id>/create/', views.MessageCreateView.as_view(), name='message_create'),
]
