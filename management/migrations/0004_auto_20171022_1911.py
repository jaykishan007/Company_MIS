# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 19:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_auto_20171022_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='report_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='management.Employee'),
        ),
    ]
