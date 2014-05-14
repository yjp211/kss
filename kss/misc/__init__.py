# -*- coding: utf-8 -*-


class Result(object):
    """
    function return result instance
    """

    def __init__(self):
        self.success = True  # True/False
        self.msg = ''        # message
        self.errno = ''      # error number
        self.exception = ''   # if have a exception, save it

    def __unicode__(self):
        if self.success:
            return u'成功：<%s>' % self.msg
        else:
            return u'失败：<%s><%s><%s>' % (self.errno, self.msg, self.exception)
