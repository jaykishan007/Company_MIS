# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-22 19:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]