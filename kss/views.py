# -*- coding:utf-8 -*-
from django.shortcuts import render
from kss.misc.debug import debug

def home(request, template='home.html'):
    """
    home index for kss
    """
    debug.view('wocao')
    debug.service('nima')
    return render(request, template)
