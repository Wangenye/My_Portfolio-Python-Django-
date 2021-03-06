# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *
from .models import Aboutme, Project, SocialLink
# Create your views here.


def index(request):

    aboutMe = Aboutme.objects.all()

    projects = Project.objects.all()

    return render(request, 'portfolio/index.html', {
        'aboutMe': aboutMe,
        'projects': projects
    })


def contactInfo(request):
    abouT = Aboutme.objects.all()
    social_links = SocialLink.objects.all()

    return render(request, 'portfolio/contactInfo_about.html', {
        'abouT': abouT,
        'social_links': social_links
    })
