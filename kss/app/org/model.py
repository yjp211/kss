# -*- coding:utf-8 -*-

from kss.misc.base.entry import BaseEntry

class Dept(BaseEntry):
    """
    部门组织结构
    """

    def __init__(self):
        self.id = ''
        self.name = ''

        self.parentId = ''
        self.users = []
        self.depts = []


class User(BaseEntry):
    """
    用户组织结构
    """

    def __init__(self):
        self.id = ''
        self.name = ''
        self.alias = ''

        self.parentId = ''



if __name__ == '__main__':
    root = Dept()
    root.id = 1
    root.name = u'撒旦发射'

    d1 = Dept()
    d1.id = 2
    d1.name = u'阿萨德发射点发'

    u1 = User()
    u1.id = 999
    u1.name = 'user1'
    u1.alias = u'砸啊'

    u2 = User()
    u2.id = 100
    u2.name = 'user2'
    u2.alias = u'123123'

    d1.users.append(u2)
    root.users.append(u1)
    root.depts.append(d1)

    print root.to_dhtmltree_json()
