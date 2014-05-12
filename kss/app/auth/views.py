# -*- coding:utf-8 -*-
from django.shortcuts import render

from kss.decorator.view import request_post

from kss.misc.debug import debug

def index(request, template='auth/login.html'):
    """
    index for login page
    """
    return render(request, template)

@request_post
def action(request):
    """
    login action
    """
    user_name = request.POST.get('username', '')
    passwd = request.POST.get('passwd', '')
    debug.view(u"<%s>认证登录")
    return render(request)