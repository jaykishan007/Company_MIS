# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date
from django.db import models

# Create your models here.


class Employee(models.Model):

    SEX = [
        ("M", "Male"),
        ("F", "Female")
    ]
    user_name = models.CharField(max_length=50)
    address = models.TextField(max_length=100)
    date = models.DateField(auto_now=True)
    sex = models.CharField(max_length=1, choices=SEX)
    salary = models.IntegerField()
    report_to = models.ForeignKey("self", blank=True, null=True)

    def __str__(self):
        return self.user_name


class Department(models.Model):

    depart_name = models.CharField(max_length=50)
    manager_to_depart = models.ForeignKey(Employee, related_name='Employee', null=True)
    manager_start_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.depart_name


class DepartmentLocation(models.Model):

    depart_object_ref = models.ForeignKey(Department, on_delete=models.CASCADE)
    depart_location = models.TextField(max_length=100)

    class Meta:
        unique_together = (('depart_object_ref', 'depart_location'),)

    def __str__(self):
        return self.depart_location + self.depart_object_ref.manager_to_depart.user_name


class Project(models.Model):
    project_name = models.CharField(max_length=50)
    depart_number = models.ForeignKey(Department, on_delete=models.CASCADE)
    employee_on_project = models.ManyToManyField(Employee)

    def __str__(self):
        return self.project_name







