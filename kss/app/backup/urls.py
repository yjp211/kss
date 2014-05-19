# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from kss.app.backup.views import backup

urlpatterns = patterns('',
    url(r'^$', backup.index, name='backup_index'),
)
