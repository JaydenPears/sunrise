# Generated by Django 4.1.6 on 2023-11-07 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_periodiclesson_day'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='end_time',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='start_time',
            new_name='start',
        ),
    ]
