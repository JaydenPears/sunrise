from django.contrib import admin

from ..models import Section


@admin.register(Section)
class SectionModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image', 'is_free', 'cost', 'is_active')
    fields = list_display

