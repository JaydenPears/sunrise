from django.db import models
from django.utils.translation import gettext_lazy as _
from .section import Section


class SectionGroup(models.Model):
    title = models.CharField(_('Title'), max_length=100)
    Section = models.ManyToManyField(to=Section, related_name='groups')

    class Meta:
        verbose_name = _('Group')
        verbose_name_plural = _('Groups')
        ordering = ('id',)

    def __str__(self):
        return f'{self.title}, Section: {self.Section}'
