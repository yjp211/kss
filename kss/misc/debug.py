# -*- coding:utf-8 -*-

import logging


logging.addLevelName(logging.DEBUG + 1, 'API')
logging.addLevelName(logging.DEBUG + 2, 'DB')
logging.addLevelName(logging.DEBUG + 3, 'CACHE')
logging.addLevelName(logging.DEBUG + 4, 'VIEW')
logging.addLevelName(logging.DEBUG + 5, 'SERVICE')



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



