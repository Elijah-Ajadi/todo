# Generated by Django 5.1.4 on 2025-01-14 22:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_Name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_Name', models.CharField(blank=True, max_length=60, null=True)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('phone_number', models.IntegerField(max_length=11, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('user_tasks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task')),
            ],
        ),
    ]
