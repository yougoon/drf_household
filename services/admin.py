
# services/admin.py
from django.contrib import admin
from .models import Service, Review

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'average_rating']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'service', 'rating', 'comment']