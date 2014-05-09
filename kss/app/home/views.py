# -*- coding:utf-8 -*-
from django.shortcuts import render


def home(reuquest, template='home/home.html'):
    """
    home index for kss
    """
    return render(reuquest, template)
