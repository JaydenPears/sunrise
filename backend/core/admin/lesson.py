from django.contrib import admin

from ..models import Lesson


@admin.register(Lesson)
class LessonModelAdmin(admin.ModelAdmin):
    list_display = ('group', 'section', 'date', 'start_time', 'end_time', 'periodic_id')
    fields = list_display
