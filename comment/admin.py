from django.contrib import admin
from .models import Comment
# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'type_id', 'created_by', 'comment', 'created_at', 'updated_at']