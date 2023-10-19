import datetime

from django.contrib import admin
from django.db import transaction

from ..models import PeriodicLesson, Lesson
from ..serializers import LessonSerializer, PeriodicLessonSerializer


@admin.register(PeriodicLesson)
class PeriodicLessonModelAdmin(admin.ModelAdmin):
    list_display = ('group', 'section', 'day', 'start_time', 'end_time', 'start_date', 'end_date')
    fields = list_display

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        end_date = obj.end_date
        start_date = obj.start_date
        Lesson.objects.filter(periodic_id=obj.pk).delete()
        with transaction.atomic():
            while start_date <= end_date:
                if start_date.weekday() == int(form.data['day']):
                    data = {
                        'group': obj.group.pk,
                        'section': obj.section.pk,
                        'date': start_date,
                        'start_time': obj.start_time,
                        'end_time': obj.end_time,
                        'periodic_id': obj.pk,
                    }
                    lesson = LessonSerializer(data=data)
                    lesson.is_valid(raise_exception=True)
                    lesson.save()
                start_date += datetime.timedelta(days=1)

