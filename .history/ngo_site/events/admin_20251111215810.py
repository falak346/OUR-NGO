from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "start_date", "end_date", "location")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("start_date",)
    search_fields = ("title", "location", "description")
