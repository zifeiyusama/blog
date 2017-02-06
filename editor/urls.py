#/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    blog.urls
    ~~~~~~~~~~~~~~

    url patterns for editor

    :copyright: (c) 2016 by zifeiyu.
    :license: MIT, see LICENSE for more details.
"""
from django.conf.urls import url, include

from .import views

app_name = 'editor'
urlpatterns = [
    url(r'^preview$', views.preview, name='preview'),
]
