#/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    wiki.admin
    ~~~~~~~~~~~~~~

    wiki admin interface

    :copyright: (c) 2016 by zifeiyu.
    :license: MIT, see LICENSE_FILE for more details.
"""
from django.conf.urls.static import static
from django.core.files.storage import DefaultStorage
from filebrowser.sites import FileBrowserSite
from .fb_actions import publish
from .settings import FILE_BROWSER_NAME, FILE_BROWSER_DIRECTORY

wiki_site = FileBrowserSite(name=FILE_BROWSER_NAME, storage=DefaultStorage())
wiki_site.directory = FILE_BROWSER_DIRECTORY

wiki_site.add_action(publish)
