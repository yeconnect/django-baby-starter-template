from django.contrib import admin
from .models import User, Room, Message

admin.site.register(User)
admin.site.register(Room)
admin.site.register(Message)
