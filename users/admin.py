# users/admin.py
from django.contrib import admin
from .models import CustomUser, Profile

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_admin', 'is_client']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio', 'profile_picture']