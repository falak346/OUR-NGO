from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Donation

@admin.register(Donation)
class DonationAdmin(ModelAdmin):
    list_display = ("name", "email", "amount", "created")
    search_fields = ("name", "email")
    list_filter = ("created",)
