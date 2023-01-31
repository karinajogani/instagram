from django.contrib import admin
from .models import DirectMessage
# Register your models here.

@admin.register(DirectMessage)
class DirectMessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'created_by', 'send_to', 'created_at', 'updated_at']
