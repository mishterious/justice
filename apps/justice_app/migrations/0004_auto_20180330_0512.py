# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-30 05:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('justice_app', '0003_auto_20180330_0409'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('improve', models.CharField(max_length=255)),
                ('my_reason', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_reason', to='justice_app.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='reason',
            name='user',
        ),
        migrations.DeleteModel(
            name='Reason',
        ),
    ]
