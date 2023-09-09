# Generated by Django 4.1.6 on 2023-09-09 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_section_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Afisha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.CharField(max_length=300, verbose_name='Description')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('date', models.DateTimeField(verbose_name='Date and time')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Created time')),
            ],
            options={
                'verbose_name': 'Afisha',
                'verbose_name_plural': 'Afishes',
                'ordering': ('-created_time',),
            },
        ),
        migrations.CreateModel(
            name='ClubInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500, verbose_name='Text')),
            ],
            options={
                'verbose_name': 'ClubInfo',
            },
        ),
        migrations.CreateModel(
            name='Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=100, verbose_name='FIO')),
                ('vk_id', models.CharField(max_length=100, verbose_name='VK id')),
                ('tg_id', models.CharField(max_length=100, verbose_name='Telegram id')),
                ('description', models.CharField(max_length=300, verbose_name='Description')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('phone', models.CharField(max_length=100, verbose_name='Phone number')),
            ],
            options={
                'verbose_name': 'Management',
                'verbose_name_plural': 'Managements',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Partner',
                'verbose_name_plural': 'Partners',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.CharField(max_length=300, verbose_name='Description')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('date', models.DateTimeField(verbose_name='Date and time')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Created time')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ('-created_time',),
            },
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=100, verbose_name='FIO')),
                ('vk_id', models.CharField(max_length=100, verbose_name='VK id')),
                ('tg_id', models.CharField(max_length=100, verbose_name='Telegram id')),
                ('description', models.CharField(max_length=300, verbose_name='Description')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('phone', models.CharField(max_length=100, verbose_name='Phone number')),
                ('Section', models.ManyToManyField(related_name='Trainer', to='core.section')),
            ],
            options={
                'verbose_name': 'Trainer',
                'verbose_name_plural': 'Trainers',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='SectionGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('Section', models.ManyToManyField(related_name='Section', to='core.section')),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Date and time')),
                ('start_time', models.TimeField(verbose_name='Start time')),
                ('end_time', models.TimeField(verbose_name='End time')),
                ('Group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Group', to='core.sectiongroup')),
            ],
            options={
                'verbose_name': 'Lesson',
                'verbose_name_plural': 'Lesson',
                'ordering': ('id',),
            },
        ),
    ]