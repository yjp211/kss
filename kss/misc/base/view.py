# -*- coding:utf-8 -*-

import inspect

from django.http.response import HttpResponseServerError

from kss.misc.debug import log_view


def view_wrap(func):
    """
    对view func进行包装
        debug日志记录
    """
    def wrapped(request, *args, **kwargs):
        # __doc__ encode as ascii
        # and we only need the first line
        doc = func.__doc__
        description = doc.strip().split('\n')[0].decode('utf-8')

        log_view.debug(u'<%s:%s> %s [ 参数 GET：%s，POST：%s ]' %
                       (func.__module__, func.__name__, description, request.GET.items(), request.POST.items()))
        try:
            response = func(request, *args, **kwargs)
            log_view.debug(u'%s [ http状态码，%s ]' % (description, response.status_code))
            return response
        except Exception, e:
            log_view.error(u'%s [ 出现异常，%s ]' % (description, e))
            return HttpResponseServerError()

    return wrapped


class BaseView(object):
    """
    所有的View都从该类继承
    """

    def __getattribute__(self, name):
        value = object.__getattribute__(self, name)
        if inspect.ismethod(value):
            if str(name).startswith('_'):
                return value
            return view_wrap(value)
        else:
            return value