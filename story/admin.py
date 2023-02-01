from django.contrib import admin
from .models import Story
# Register your models here.

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ['story_id', 'image', 'title', 'created_by', 'viewed_by', 'created_at', 'expires_at']
