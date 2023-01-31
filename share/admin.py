from django.contrib import admin
from .models import Share
# Register your models here.


@admin.register(Share)
class ShareAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'type_id', 'created_by', 'share_to', 'created_at', 'updated_at']
   