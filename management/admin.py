# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from management import models

from django.contrib import admin

# Register your models here.

admin.site.register(models.Employee)
admin.site.register(models.Department)
admin.site.register(models.DepartmentLocation)
admin.site.register(models.Project)
