# -*- coding:utf-8 -*-

import logging

logging.API = logging.DEBUG + 1
logging.DB = logging.DEBUG + 2
logging.CACHE = logging.DEBUG + 3
logging.VIEW = logging.DEBUG + 4
logging.SERVICE = logging.DEBUG + 5

logging.addLevelName(logging.API, 'API')
logging.addLevelName(logging.DB, 'DB')
logging.addLevelName(logging.CACHE, 'CACHE')
logging.addLevelName(logging.VIEW, 'VIEW')
logging.addLevelName(logging.SERVICE, 'SERVICE')



def logwrap(self, level):
    def func(msg, *args, **kwargs):
        return self._log(level, msg, args, **kwargs)
    return func

def getattrwrap(self, item):
    """
    没有属性时触发
    """
    level = logging.getLevelName(str(item).upper())
    if isinstance(level, basestring) and level.startswith('Level '):
        raise AttributeError

    return logwrap(self, level)

logging.Logger.__getattr__ = getattrwrap

debug = logging.getLogger('debug')



