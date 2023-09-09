# Generated by Django 4.1.6 on 2023-09-09 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_delete_afisha_post_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(max_length=100, verbose_name='Job')),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=100, verbose_name='FIO')),
                ('vk_id', models.CharField(max_length=100, verbose_name='VK id')),
                ('tg_id', models.CharField(max_length=100, verbose_name='Telegram id')),
                ('description', models.CharField(max_length=300, verbose_name='Description')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('phone', models.CharField(max_length=100, verbose_name='Phone number')),
                ('Section', models.ManyToManyField(related_name='personal', to='core.section')),
                ('job', models.ManyToManyField(related_name='personal', to='core.job')),
            ],
            options={
                'verbose_name': 'Personal',
                'ordering': ('id',),
            },
        ),
        migrations.DeleteModel(
            name='Management',
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ('id',), 'verbose_name': 'Lesson', 'verbose_name_plural': 'Lessons'},
        ),
        migrations.AddField(
            model_name='post',
            name='short_description',
            field=models.CharField(default='', max_length=300, verbose_name='Short description'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='Group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lessons', to='core.sectiongroup'),
        ),
        migrations.AlterField(
            model_name='sectiongroup',
            name='Section',
            field=models.ManyToManyField(related_name='groups', to='core.section'),
        ),
        migrations.DeleteModel(
            name='Trainer',
        ),
    ]