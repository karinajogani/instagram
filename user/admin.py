from django.contrib import admin
from .models import User
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'gender', 'email_id', 'password', 'account_type', 'created_at', 'updated_at']