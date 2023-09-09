from django.contrib import admin

from ..models import SectionGroup


@admin.register(SectionGroup)
class SectionGroupModelAdmin(admin.ModelAdmin):
    list_display = ('title', )
    fields = ('title', 'Section')
    filter_horizontal = ('Section',)
