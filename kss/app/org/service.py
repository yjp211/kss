# -*- coding:utf-8 -*-

from kss.misc import Result
from kss.misc.base.service import BaseService

from kss.app.org.model import Dept, User


__all__ = ['org_service']


class OrgService(BaseService):


    def get_root_dept(self):
        """
        获取根部门
        """
        ret = Result()

        virtual = Dept()
        virtual.id = 0

        root = Dept()
        root.id = 1
        root.name = u'根部门'
        root.open = 1

        d1 = Dept()
        d1.id = 2
        d1.name = u'事业部'

        u1 = User()
        u1.id = 999
        u1.name = 'user1'
        u1.alias = u'阿斯蒂芬'

        u2 = User()
        u2.id = 100
        u2.name = 'user2'
        u2.alias = u'阿萨德分享'

        #d1.users.append(u2)
        root.users.append(u1)
        root.depts.append(d1)

        virtual.depts.append(root)

        ret.data['root_dept'] = virtual
        return ret

    def get_dept_by_id(self, dept_id):
        """
        根据ID获取部门信息
        """
        ret = Result()

        dept = Dept()
        dept.id = dept_id
        dept.name = u'办公司'

        child_dept = Dept()
        child_dept.id = 333
        child_dept.name = u'子部门们'

        u1 = User()
        u1.id = 111
        u1.name = 'user1111'
        u1.alias = u'尼玛'

        u2 = User()
        u2.id = 22222
        u2.name = 'userasdf2'
        u2.alias = u'心大事发生地方'

        dept.users.append(u1)
        dept.users.append(u2)
        dept.depts.append(child_dept)

        ret.data['dept'] = dept
        return ret

    def all_user(self):
        """
        获取所有用户
        """
        ret = Result()
        return ret


org_service = OrgService()