# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2016-06-15 15:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0003_auto_20160615_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='cop',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='result_status',
            field=models.CharField(max_length=200),
        ),
    ]
