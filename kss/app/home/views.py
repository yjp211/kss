# -*- coding:utf-8 -*-
from django.shortcuts import render


def home(request, template='home/home.html'):
    """
    home index for kss
    """
    return render(request, template)
