# Generated by Django 5.1.4 on 2025-01-16 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_category_task_task_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='task_type',
        ),
    ]