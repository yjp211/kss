# -*- coding:utf-8 -*-

"""
提供各种试图的装饰器
"""

from django.http.response import HttpResponseNotAllowed

from kss.misc.debug import log_view

__all__ = ['require_get', 'require_post']

def require_method(method):
    """
    request的请求类型必须为 [method]
    @param method: POST|GET
    """
    def func(function=None):
        def _filter(self, request, *args, **kwargs):

            if request.method != method:
                log_view.error(u"request<%s:%s>请求类型必须为<%s>，当前为<%s>" %
                           (function.__module__, function.__name__, method, request.method))
                return HttpResponseNotAllowed([method])
            else:
                return function(self, request, *args, **kwargs)

        # 将__doc__ 传递下去，否则会引起异常
        _filter.__doc__ = function.__doc__
        _filter.__module__ = function.__module__
        _filter.__name__ = function.__name__

        return _filter
    return func

require_get = require_method('GET')

require_post = require_method('POST')