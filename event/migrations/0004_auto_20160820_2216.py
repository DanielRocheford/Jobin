# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-20 22:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20160814_1848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='start',
        ),
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]
