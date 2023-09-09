from django.contrib import admin

from ..models import Lesson


@admin.register(Lesson)
class LessonModelAdmin(admin.ModelAdmin):
    list_display = ('Group', 'date', 'start_time', 'end_time')
    fields = list_display
