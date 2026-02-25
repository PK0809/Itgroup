from django.contrib import admin
from .models import ContactMessage, CareerApplication


@admin.register(ContactMessage)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    search_fields = ("name", "email")


@admin.register(CareerApplication)
class CareerAdmin(admin.ModelAdmin):
    list_display = ("full_name", "position", "created_at")
    search_fields = ("full_name", "position")