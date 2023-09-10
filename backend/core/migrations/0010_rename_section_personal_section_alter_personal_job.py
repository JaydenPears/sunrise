# Generated by Django 4.1.6 on 2023-09-09 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_job_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personal',
            old_name='Section',
            new_name='section',
        ),
        migrations.AlterField(
            model_name='personal',
            name='job',
            field=models.ManyToManyField(related_name='personal', to='core.job'),
        ),
    ]
