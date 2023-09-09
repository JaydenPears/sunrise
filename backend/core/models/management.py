from django.db import models
from django.utils.translation import gettext_lazy as _


class Management(models.Model):
    fio = models.CharField(_('FIO'), max_length=100)
    vk_id = models.CharField(_('VK id'), max_length=100)
    tg_id = models.CharField(_('Telegram id'), max_length=100)
    description = models.CharField(_('Description'), max_length=300)
    image = models.ImageField(_('Image'))
    phone = models.CharField(_('Phone number'), max_length=100)

    class Meta:
        verbose_name = _('Management')
        verbose_name_plural = _('Managements')
        ordering = ('id',)

    def __str__(self):
        return f'{self.fio}'
