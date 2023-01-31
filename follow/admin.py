from django.contrib import admin
from .models import Follow
# Register your models here.

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ['id', 'following','created_by', 'created_at', 'updated_at']
#  'updated_by', 