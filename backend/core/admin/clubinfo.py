from django.contrib import admin

from ..models import ClubInfo


@admin.register(ClubInfo)
class ClubInfoModelAdmin(admin.ModelAdmin):
    list_display = ('text',)
    fields = list_display

