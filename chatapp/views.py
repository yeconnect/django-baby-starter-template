from django.shortcuts import render
from .models import User, Room, Message
from rest_framework.response import Response
from rest_framework.views import APIView


# あるユーザーが所属するチャットルーム一覧を表示するAPI
class RoomListView(APIView):
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        rooms = user.rooms.all()
        res_rooms = []
        for room in rooms:
            res_room = {
                'id': room.id,
                'name': room.name,
                'created_at': room.created_at,
                'updated_at': room.updated_at,
                'users': room.users.all().values('name'),
            }
            res_rooms.append(res_room)
        return Response(res_rooms)


# あるルームのメッセージ一覧を表示するAPI
class MessageListView(APIView):
    def get(self, request, room_id):
        messages = Message.objects.filter(room_id=room_id)
        res_messages = []
        for message in messages:
            res_message = {
                'id': message.id,
                'message': message.message,
                'created_at': message.created_at,
                'updated_at': message.updated_at,
                'user': message.user.name,
                'room': message.room.name,
            }
            res_messages.append(res_message)
        return Response(res_messages)


# あるルームにメッセージを送信するAPI
class MessageCreateView(APIView):
    def post(self, request, room_id):
        message = Message.objects.create(
            message=request.data['message'],
            user=User.objects.get(id=request.data['user_id']),
            room=Room.objects.get(id=room_id),
        )
        res_message = {
            'id': message.id,
            'message': message.message,
            'created_at': message.created_at,
            'updated_at': message.updated_at,
            'user': message.user.name,
            'room': message.room.name,
        }
        return Response(res_message)