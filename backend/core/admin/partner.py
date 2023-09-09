from django.contrib import admin

from ..models import Partner


@admin.register(Partner)
class PartnerModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    fields = list_display
