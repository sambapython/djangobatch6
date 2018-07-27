# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-27 03:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_studyhall_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='created_by',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.UserProfile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 27, 8, 57, 12, 162000)),
        ),
        migrations.AddField(
            model_name='enquiry',
            name='created_by',
            field=models.ForeignKey(blank=True, default=2, on_delete=django.db.models.deletion.CASCADE, to='app1.UserProfile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enquiry',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 27, 8, 57, 12, 162000)),
        ),
        migrations.AddField(
            model_name='expenses',
            name='created_by',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.UserProfile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expenses',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 27, 8, 57, 12, 162000)),
        ),
        migrations.AddField(
            model_name='student',
            name='created_by',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.UserProfile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 27, 8, 57, 12, 162000)),
        ),
        migrations.AddField(
            model_name='studyhall',
            name='created_by',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.UserProfile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studyhall',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 27, 8, 57, 12, 162000)),
        ),
    ]