from django.contrib import admin
from .models import Post
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['post_id', 'photo', 'caption', 'created_by', 'created_at', 'updated_at']
# 'updated_by',