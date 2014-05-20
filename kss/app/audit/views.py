# -*- coding:utf-8 -*-
from django.shortcuts import render

from kss.misc.base.view import BaseView

__all__ = ['audit']

class AuditView(BaseView):
    """
    日志审计
    """

    def index(self, request, template='audit/audit_index.html'):
        """
        日志审计
        """
        return render(request, template)


audit = AuditView()