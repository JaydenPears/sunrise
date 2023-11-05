from django.contrib import admin

from ..models import SectionGroup


@admin.register(SectionGroup)
class SectionGroupModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_section')
    fields = ('title', 'section')
    filter_horizontal = ('section',)

    def get_section(self, obj):
        return "\n".join([p.name for p in obj.section.all()])
