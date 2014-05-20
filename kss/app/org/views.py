# -*- coding:utf-8 -*-
from django.shortcuts import render

from kss.misc.base.view import BaseView

__all__ = ['org']

class OrgView(BaseView):
    """
    用户组织结构管理
    """

    def index(self, request, template='org/org_index.html'):
        """
        用户组织管理
        """
        return render(request, template)


org = OrgView()