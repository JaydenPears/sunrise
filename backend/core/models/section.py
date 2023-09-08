from django.db import models
from django.utils.translation import gettext_lazy as _


class Section(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    description = models.CharField(_('Description'),max_length=300)
    image = models.ImageField(_('Image'))

    is_free = models.BooleanField(_('Is free?'), default=True)
    cost = models.CharField(_('Cost'), max_length=100)
    is_active = models.BooleanField(_('Is active'), default=True)
