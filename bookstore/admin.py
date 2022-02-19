from django.contrib import admin

# Register your models here.
from .models import PaymentHistory, Plan

admin.site.register(PaymentHistory)
admin.site.register(Plan)