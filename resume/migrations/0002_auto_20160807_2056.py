# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-07 20:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20160807_2056'),
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('award_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('description', models.TextField()),
                ('experience_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('program', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=100)),
                ('start', models.DateField()),
                ('end', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='resume',
            name='file_resume',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='resume',
            name='last_updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='resume',
            name='student',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='student.Student'),
        ),
        migrations.AddField(
            model_name='skill',
            name='resume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.Resume'),
        ),
        migrations.AddField(
            model_name='school',
            name='resume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.Resume'),
        ),
        migrations.AddField(
            model_name='language',
            name='resume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.Resume'),
        ),
        migrations.AddField(
            model_name='experience',
            name='resume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.Resume'),
        ),
        migrations.AddField(
            model_name='award',
            name='resume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.Resume'),
        ),
    ]
