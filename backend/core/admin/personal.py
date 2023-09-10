from django.contrib import admin

from ..models import Personal


@admin.register(Personal)
class PersonalModelAdmin(admin.ModelAdmin):
    list_display = ('fio', 'vk_id', 'tg_id', 'description', 'image', 'phone')
    fields = ('section', 'fio', 'vk_id', 'tg_id', 'description', 'image', 'phone', 'job')
    filter_horizontal = ('job', 'section')
