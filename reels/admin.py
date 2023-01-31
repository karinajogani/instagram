from django.contrib import admin
from .models import Reels
# Register your models here.

@admin.register(Reels)
class ReelsAdmin(admin.ModelAdmin):
    list_display = ['id', 'video', 'caption', 'created_by', 'viewed_by', 'created_at', 'updated_at']