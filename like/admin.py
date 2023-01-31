from django.contrib import admin
from .models import Like
# Register your models here.

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'type_id', 'created_at', 'updated_at', 'created_by']
