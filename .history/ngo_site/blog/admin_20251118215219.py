from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Post

@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_display = ("title", "status", "published_at")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("status", "published_at")
    search_fields = ("title", "body")
