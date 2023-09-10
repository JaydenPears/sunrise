from django.db import models
from django.utils.translation import gettext_lazy as _


class Partner(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    image = models.ImageField(_('Image'), blank=True, upload_to='images/')

    class Meta:
        verbose_name = _('Partner')
        verbose_name_plural = _('Partners')
        ordering = ('id',)

    def __str__(self):
        return f'{self.name}'
