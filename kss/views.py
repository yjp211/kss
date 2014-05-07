# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.core.cache import  cache
from kss.misc.debug import debug

def home(reuquest, template='home.html'):
    """
    home index for kss
    """
    print cache.keys('*')
    return render(reuquest, template)
