from django.db import models
from django.utils.translation import gettext_lazy as _
from .section import Section


class Job(models.Model):
    text = models.CharField(_('Text'), max_length=100)

    def __str__(self):
        return f'{self.text}'


class Personal(models.Model):
    section = models.ManyToManyField(to=Section, related_name='personal', blank=True)
    fio = models.CharField(_('FIO'), max_length=100)
    vk_id = models.CharField(_('VK id'), max_length=100, blank=True)
    tg_id = models.CharField(_('Telegram id'), max_length=100, blank=True)
    description = models.CharField(_('Description'), max_length=300)
    image = models.ImageField(_('Image'), blank=True, upload_to='media/')
    phone = models.CharField(_('Phone number'), max_length=100)
    job = models.ManyToManyField(to=Job, related_name='personal')

    class Meta:
        verbose_name = _('Personal')
        ordering = ('id',)

    def __str__(self):
        return f'{self.fio}'
