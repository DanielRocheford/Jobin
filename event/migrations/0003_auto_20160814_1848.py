# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-14 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20160814_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='start',
            field=models.DateTimeField(null=True),
        ),
    ]