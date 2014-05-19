# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from kss.app.police.views import police

urlpatterns = patterns('',
    url(r'^$', police.index, name='police_index'),
)
