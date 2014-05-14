# -*- coding:utf-8 -*-

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from kss.decorator.view import require_post

from kss.misc.base.view import BaseView

from kss.app.auth.service import service as auth_service

__all__ = ['auth']

class AuthView(BaseView):
    """
    认证试图
    """

    def index(self, request, template='auth/login.html'):
        """
        进入认证界面
        """
        return render(request, template)


    @require_post
    def action(self, request):
        """
        认证用户
        """

        username = request.POST.get('username', '')
        passwd = request.POST.get('passwd', '')

        ret = auth_service.auth_user(username, passwd)

        if ret.success:
            messages.success(request, u'%s认证用户成功' % username)
            return redirect(reverse('home_index'))
        else:
            messages.error(request, u'%s认证用户失败，%s' % (username, ret.msg))
            return redirect(reverse('login_index'))


auth = AuthView()