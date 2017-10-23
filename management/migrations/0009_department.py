# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 19:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0008_auto_20171022_1928'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depart_name', models.CharField(max_length=50)),
                ('manager_to_depart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.Employee')),
            ],
        ),
    ]