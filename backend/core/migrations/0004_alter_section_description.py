# Generated by Django 3.2.20 on 2023-11-08 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_end_time_lesson_end_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='description',
            field=models.TextField(max_length=300, verbose_name='Description'),
        ),
    ]