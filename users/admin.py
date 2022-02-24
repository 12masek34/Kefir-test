from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


User = get_user_model()

@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ["id", "first_name", "last_name", "email", 'username', 'phone']