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
    my_logo = models.CharField(
        max_length=10,
        blank=False,
    )
    skills = models.TextField(max_length=500)
    profile_image = models.ImageField(upload_to='profile_pic')
    cV = models.FileField(upload_to='CVfolder')

    def __str__(self):
        return self.f_name


class Project(models.Model):
    name = models.CharField(max_length=100)
    project_image = models.ImageField(upload_to='project_pics',
                                      blank=False,
                                      default=None)
    demo_url = models.URLField(max_length=300, blank=True)
    git_url = models.URLField(max_length=300, blank=True)
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


class SocialLink(models.Model):
    name = models.CharField(max_length=20, default="Social media Links")
    facebook = models.URLField(max_length=300, blank=True)
    github = models.URLField(max_length=300, blank=True)
    twitter = models.URLField(max_length=300, blank=True)
    instagram = models.URLField(max_length=300, blank=True)
    linkedLn = models.URLField(max_length=300, blank=True)

    def __str__(self):
        return self.name
