from django.contrib import admin

# Register your models here.
from .models import ChatappUser
from .models import ChatappMessage


admin.site.register(ChatappUser)
admin.site.register(ChatappMessage)