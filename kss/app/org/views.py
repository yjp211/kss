# -*- coding:utf-8 -*-
from django.shortcuts import render, HttpResponse, Http404

from kss.misc.base.view import BaseView

from kss.app.org.service import org_service

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


    def load_root(self,request):
        """
        获取根部门
            @return json
        """
        ret = org_service.get_root_dept()
        if ret.success:
            return HttpResponse(ret.data['root_dept'].to_dhtmltree_json())
        else:
            return Http404()

    def load_dept(self, request):
        """
        加载部门信息
        """
        dept_id = request.GET.get('id')
        dept_id = dept_id.replace('%', '\\')
        dept_id = dept_id.decode('unicode_escape').encode('utf-8')
        ret = org_service.get_dept_by_id(dept_id)
        if ret.success:
            return HttpResponse(ret.data['dept'].to_dhtmltree_json())
        else:
            return Http404()


org = OrgView()