import datetime

from django.db import models, transaction
from django.utils.translation import gettext_lazy as _

from . import Section
from .group import SectionGroup


class DayOfWeak(models.TextChoices):
    MN = 0, _('Понедельник')
    TU = 1, _('Вторник')
    WN = 2, _('Среда')
    TH = 3, _('Четверг')
    FR = 4, _('Пятница')
    ST = 5, _('Суббота')
    SU = 6, _('Воскресенье')


class PeriodicLesson(models.Model):
    group = models.ForeignKey(to=SectionGroup, related_name='periodiclessons', null=True, on_delete=models.SET_NULL)
    section = models.ForeignKey(to=Section, related_name='periodiclessons', null=True, on_delete=models.SET_NULL)
    day = models.CharField(_('Day of weak'), max_length=11, choices=DayOfWeak.choices, default=DayOfWeak.MN)
    start_time = models.TimeField(_('Start time'))
    end_time = models.TimeField(_('End time'))
    start_date = models.DateField(_('Start date'))
    end_date = models.DateField(_('End date'))

    class Meta:
        verbose_name = _('PeriodicLesson')
        verbose_name_plural = _('PeriodicLessons')
        ordering = ('id',)

    def __str__(self):
        return f'Group {self.group}, Day: {self.day}'
