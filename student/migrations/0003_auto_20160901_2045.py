# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-01 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20160807_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='country',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='graduate',
            field=models.BooleanField(default=False),
        ),
    ]
