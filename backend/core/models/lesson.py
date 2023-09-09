from django.db import models
from django.utils.translation import gettext_lazy as _
from .group import SectionGroup


class Lesson(models.Model):
    Group = models.ForeignKey(to=SectionGroup, related_name='Group', null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(_('Date and time'))
    start_time = models.TimeField(_('Start time'))
    end_time = models.TimeField(_('End time'))

    class Meta:
        verbose_name = _('Lesson')
        verbose_name_plural = _('Lesson')
        ordering = ('id',)

    def __str__(self):
        return f'Group {self.Group}, Date: {self.date}'
