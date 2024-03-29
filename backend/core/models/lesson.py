from django.db import models
from django.utils.translation import gettext_lazy as _

from . import Section
from .group import SectionGroup
from .periodiclesson import PeriodicLesson


class Lesson(models.Model):
    group = models.ForeignKey(to=SectionGroup, related_name='lessons', null=True, on_delete=models.SET_NULL)
    section = models.ForeignKey(to=Section, related_name='lessons', null=True, on_delete=models.SET_NULL)
    date = models.DateField(_('Date'))
    start = models.TimeField(_('Start time'))
    end = models.TimeField(_('End time'))

    periodic_id = models.ForeignKey(to=PeriodicLesson, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = _('Lesson')
        verbose_name_plural = _('Lessons')
        ordering = ('id',)

    def get_start_time(self):
        return self.start.strftime("%H:%M")

    def get_end_time(self):
        return self.end.strftime("%H:%M")

    def __str__(self):
        return f'Group {self.group}, Date: {self.date}'

    def title(self):
        return f'{self.get_start_time()}\n-\n{self.get_end_time()}'
