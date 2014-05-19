# -*- coding:utf-8 -*-
from django.shortcuts import render

from kss.misc.base.view import BaseView

__all__ = ['home']

class DeptView(BaseView):
    """
    部门管理
    """

    def index(self, request, template='dept/dept_index.html'):
        """
        部门管理
        """
        return render(request, template)


dept = DeptView()