# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2016-06-14 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(blank=True, max_length=50)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('father_name', models.CharField(blank=True, max_length=50)),
                ('roll_no', models.CharField(blank=True, max_length=10)),
                ('student_status', models.CharField(blank=True, max_length=50)),
                ('course_code', models.IntegerField()),
                ('institution_code', models.IntegerField()),
                ('noe031i', models.CharField(max_length=3)),
                ('noe031e', models.CharField(max_length=3)),
                ('nec309i', models.CharField(max_length=3)),
                ('nec309e', models.CharField(max_length=3)),
                ('ncs301i', models.CharField(max_length=3)),
                ('ncs301e', models.CharField(max_length=3)),
                ('ncs302i', models.CharField(max_length=3)),
                ('ncs302e', models.CharField(max_length=3)),
                ('ncs303i', models.CharField(max_length=3)),
                ('ncs303e', models.CharField(max_length=3)),
                ('nhu301i', models.CharField(max_length=3)),
                ('nhu301e', models.CharField(max_length=3)),
                ('nhu402i', models.CharField(max_length=3)),
                ('nhu402e', models.CharField(max_length=3)),
                ('nas401i', models.CharField(max_length=3)),
                ('nas401e', models.CharField(max_length=3)),
                ('ncs401i', models.CharField(max_length=3)),
                ('ncs401e', models.CharField(max_length=3)),
                ('ncs402i', models.CharField(max_length=3)),
                ('ncs402e', models.CharField(max_length=3)),
                ('ncs403i', models.CharField(max_length=3)),
                ('ncs403e', models.CharField(max_length=3)),
                ('nec409i', models.CharField(max_length=3)),
                ('nec409e', models.CharField(max_length=3)),
                ('nec359pi', models.CharField(max_length=3)),
                ('nec359pe', models.CharField(max_length=3)),
                ('ncs351pi', models.CharField(max_length=3)),
                ('ncs351pe', models.CharField(max_length=3)),
                ('ncs353pi', models.CharField(max_length=3)),
                ('ncs353pe', models.CharField(max_length=3)),
                ('ncs355pi', models.CharField(max_length=3)),
                ('ncs355pe', models.CharField(max_length=3)),
                ('nec459pi', models.CharField(max_length=3)),
                ('nec459pe', models.CharField(max_length=3)),
                ('ncs451pi', models.CharField(max_length=3)),
                ('ncs451pe', models.CharField(max_length=3)),
                ('ncs453pi', models.CharField(max_length=3)),
                ('ncs453pe', models.CharField(max_length=3)),
                ('ncs455pi', models.CharField(max_length=3)),
                ('ncs455pe', models.CharField(max_length=3)),
                ('gp301', models.CharField(max_length=3)),
                ('gp401', models.CharField(max_length=3)),
                ('hvp', models.CharField(max_length=10)),
                ('cs', models.CharField(max_length=10)),
                ('result_status', models.CharField(max_length=50)),
                ('cop', models.CharField(blank=True, max_length=50)),
                ('total_internal', models.IntegerField()),
                ('totlal_external', models.IntegerField()),
                ('total_marks', models.IntegerField()),
            ],
        ),
    ]
