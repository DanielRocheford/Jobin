# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-01 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_auto_20160820_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='country',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
