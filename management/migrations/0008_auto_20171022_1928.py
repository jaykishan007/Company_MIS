# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 19:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0007_auto_20171022_1925'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='date_of_join',
            new_name='date',
        ),
    ]
