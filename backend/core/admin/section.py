from django.contrib import admin

from ..models import Section


@admin.register(Section)
class SectionModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'image', 'is_free', 'cost', 'is_active')
    readonly_fields = ['id']
    fields = ('id', 'name', 'description', 'image', 'is_free', 'cost', 'is_active')

