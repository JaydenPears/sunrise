# Generated by Django 4.1.6 on 2023-09-09 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ('id',), 'verbose_name': 'Section', 'verbose_name_plural': 'Sections'},
        ),
    ]
