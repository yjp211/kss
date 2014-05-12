# -*- coding:utf-8 -*-

"""
提供各种试图的装饰器
"""

from django.http.response import HttpResponseNotAllowed

from kss.misc.debug import debug

__all__ = ['request_get', 'request_post']

def request_method(method):
    """
    request的请求类型必须为 [method]
    @param method: POST|GET
    """
    def func(function=None):
        def _filter(request, *args, **kwargs):
            if request.method != method:
                debug.view(u"request<%s:%s>请求类型必须为<%s>，当前为<%s>" %
                           (function.__module__, function.__name__, method, request.method))
                return HttpResponseNotAllowed([method])
            else:
                return function(request, *args, **kwargs)
        return _filter
    return func

request_get = request_method('GET')

request_post = request_method('POST')