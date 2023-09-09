from django.contrib import admin

from ..models import Job


@admin.register(Job)
class JobModelAdmin(admin.ModelAdmin):
    list_display = ('job',)
    fields = list_display
