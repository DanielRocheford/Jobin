# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-01 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_application_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='programs',
            field=models.CharField(default='ALL', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='schools',
            field=models.CharField(default='ALL', max_length=200, null=True),
        ),
    ]