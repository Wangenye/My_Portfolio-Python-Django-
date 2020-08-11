# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Aboutme(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    other_name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    about = models.TextField(blank=False)
    skills = models.TextField()
    image = models.ImageField(upload_to='images/myimage')

    def __str__(self):
        return self.f_name


class Project(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='images/myimage')
    url = models.URLField()
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Contact(models.Model):
    sender_name = models.CharField(max_length=100)
    sender_email = models.EmailField()
    sender_phoneNo = models.IntegerField()
    message = models.TextField()
    header = models.CharField(max_length=100)

    def __str__(self):
        return self.sender_email
