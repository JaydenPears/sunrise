from django.db import models
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    title = models.CharField(_('Title'), max_length=100)
    description = models.CharField(_('Description'),max_length=300)
    image = models.ImageField(_('Image'))
    date = models.DateTimeField(_('Date and time'))
    created_time = models.DateTimeField(_('Created time'), auto_now_add=True)

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        ordering = ('-created_time',)

    def __str__(self):
        return f'{self.title}, Date: {self.date}'

