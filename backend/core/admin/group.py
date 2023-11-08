from django.contrib import admin

from ..models import SectionGroup


@admin.register(SectionGroup)
class SectionGroupModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_section')
    readonly_fields = ['id']
    fields = ('id', 'title', 'section')
    filter_horizontal = ('section',)

    def get_section(self, obj):
        return "\n".join([p.name for p in obj.section.all()])
