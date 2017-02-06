#/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    wiki.settings
    ~~~~~~~~~~~~~~

    custom settings in wiki

    :copyright: (c) 2016 by zifeiyu.
    :license: MIT, see LICENSE_FILE for more details.
"""
import os
from django.conf import settings

FILE_BROWSER_NAME = 'wiki'
FILE_BROWSER_DIRECTORY = 'wiki/'

PARENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI_DIR = os.path.join(PARENT_DIR, 'wiki')
WIKI_MEDIA_ROOT = os.path.join(WIKI_DIR, 'templates', 'wiki', 'html')
WIKI_MEDIA_URL = '/wiki/'

SPHINX_FROM_DIR = os.path.join(settings.MEDIA_ROOT, FILE_BROWSER_DIRECTORY)
SPHINX_TO_DIR = os.path.join(WIKI_DIR, 'source')
