#/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    edior.utils
    ~~~~~~~~~~~~~~

    utils used by widgets

    :copyright: (c) 2016 by zifeiyu.
    :license: MIT, see LICENSE for more details.
"""
from django.template import loader


def init_editor(**context):
    INIT_TEMPLATE = loader.get_template('editor/editor.html', context)
    return INIT_TEMPLATE.render()
