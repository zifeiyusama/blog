#/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    wiki.urls
    ~~~~~~~~~~~~~~

    url patterns for wiki

    :copyright: (c) 2016 by zifeiyu.
    :license: MIT, see LICENSE for more details.
"""
from django.conf.urls.static import static
from .settings import WIKI_MEDIA_ROOT, WIKI_MEDIA_URL

app_name = 'wiki'
urlpatterns = static(WIKI_MEDIA_URL, document_root=WIKI_MEDIA_ROOT)
