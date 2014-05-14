# -*- coding:utf-8 -*-
from django.shortcuts import render

from kss.decorator.view import require_post

from kss.misc.debug import log_debug

def index(request, template='auth/login.html'):
    """
    index for login page
    """
    return render(request, template)

@require_post
def action(request):
    """
    login action
    """
    user_name = request.POST.get('username', '')
    passwd = request.POST.get('passwd', '')
    log_debug.view(u"<%s>认证登录")
    return render(request)