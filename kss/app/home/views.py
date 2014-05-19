# -*- coding:utf-8 -*-
from django.shortcuts import render

from kss.misc.base.view import BaseView

__all__ = ['home']

class HomeView(BaseView):
    """
    主页试图类
    """

    def index(self, request, template='home/index2.html'):
        """
        主页
        """
        return render(request, template)


home = HomeView()