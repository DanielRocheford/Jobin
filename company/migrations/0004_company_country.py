# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-01 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20160807_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='country',
            field=models.CharField(max_length=50, null=True),
        ),
    ]