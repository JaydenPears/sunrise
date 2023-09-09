from django.db import models
from django.utils.translation import gettext_lazy as _


class ClubInfo(models.Model):
    text = models.CharField(_('Text'), max_length=500)

    class Meta:
        verbose_name = _('ClubInfo')

    def __str__(self):
        return f'{self.text}'
