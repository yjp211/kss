# -*- coding:utf-8 -*-

import json

class BaseEntry(dict):
    """
    自定义数据模型的基础类
    """

    def __setattr__(self, key, value):
        return self.__setitem__(key, value)

    def __getattr__(self, item):
        return self.__getitem__(item)

    def to_json(self):
        """
        将object转换为json对象
        """
        return json.dumps(self)


if __name__ == '__main__':
    o = BaseEntry()
    o['a'] = 4
    print o.a
    o.b = 3
    a1 = BaseEntry()
    a2 = BaseEntry()
    a3 = BaseEntry()
    a1.a1 = 111
    a2.a2 = 2222
    a3.a3 = {'c':[12,345], 'd':1}

    o.l = [a1,a2,a3]
    o['haha'] = True

    print o.items()
    print o.to_json()