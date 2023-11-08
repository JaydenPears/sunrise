from django.db import models
from django.utils.translation import gettext_lazy as _


class Section(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    description = models.TextField(_('Description'), max_length=300)
    image = models.ImageField(_('Image'), blank=True, upload_to='images/')
    is_free = models.BooleanField(_('Is free?'), default=True)
    cost = models.CharField(_('Cost'), max_length=100, blank=True)
    is_active = models.BooleanField(_('Is active'), default=True)

    class Meta:
        verbose_name = _('Section')
        verbose_name_plural = _('Sections')
        ordering = ('id',)

    def __str__(self):
        return f'{self.name}'
