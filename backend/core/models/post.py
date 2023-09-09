from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.TextChoices):
    POST = 'post', _('Post')
    AFISHA = 'afisha', _('Afisha')


class Post(models.Model):
    title = models.CharField(_('Title'), max_length=100)
    description = models.CharField(_('Description'), max_length=300)
    short_description = models.CharField(_('Short description'), max_length=300)
    image = models.ImageField(_('Image'), blank=True)
    date = models.DateTimeField(_('Date and time'))
    created_time = models.DateTimeField(_('Created time'), auto_now_add=True)
    category = models.CharField(_('Category'), choices=Category.choices, default=Category.POST, max_length=50)

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        ordering = ('-created_time',)

    def __str__(self):
        return f'{self.title}, Date: {self.date}'

