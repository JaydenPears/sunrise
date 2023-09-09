from django.contrib import admin

from ..models import Post


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'short_description', 'category', 'image', 'date', 'created_time')
    fields = ('title', 'description', 'short_description', 'category', 'image', 'date')
