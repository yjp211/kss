# -*- coding:utf-8 -*-
from django.shortcuts import render
from kss.misc.debug import debug

def home(reuquest, template='home.html'):
    """
    home index for kss
    """
    debug.view('wocao')
    debug.service('nima')
    return render(reuquest, template)
