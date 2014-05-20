# -*- coding:utf-8 -*-
from django.shortcuts import render

from kss.misc.base.view import BaseView

__all__ = ['police']

class PoliceView(BaseView):
    """
    策略管理
    """

    def index(self, request, template='police/police_index.html'):
        """
        策略管理
        """
        return render(request, template)


police = PoliceView()