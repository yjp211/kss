# -*- coding:utf-8 -*-
from django.shortcuts import render

from kss.misc.base.view import BaseView

__all__ = ['home']

class UserView(BaseView):
    """
    用户管理
    """

    def index(self, request, template='user/user_index.html'):
        """
        用户管理
        """
        return render(request, template)


user = UserView()