#/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    wiki.fb_actions
    ~~~~~~~~~~~~~~

    custom actions used in wiki's file-browser admin interface

    :copyright: (c) 2016 by zifeiyu.
    :license: MIT, see LICENSE for more details.
"""
from .settings import SPHINX_FROM_DIR, SPHINX_TO_DIR, PARENT_DIR, WIKI_DIR
import shutil, os
from .utils import sphinx_build
from django.contrib import messages

def publish(request, fileobjects):
    for file_object in fileobjects:
        source_file = PARENT_DIR + file_object.url
        target_file = os.path.join(SPHINX_TO_DIR, os.path.basename(source_file))
        shutil.copyfile(source_file, target_file)
    if not sphinx_build('cd ' + WIKI_DIR + '; make html'):
        messages.add_message(request, messages.SUCCESS, '发布成功')
    else:
        messages.add_message(request, messages.ERROR, '发布失败')
publish.short_description = '发布'
