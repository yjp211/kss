# -*- coding:utf-8 -*-
from django.shortcuts import render

from kss.misc.base.view import BaseView

__all__ = ['backup']

class BackupView(BaseView):
    """
    数据备份管理
    """

    def index(self, request, template='backup/backup_index.html'):
        """
        数据备份
        """
        return render(request, template)


backup = BackupView()