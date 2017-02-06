#/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    wiki.utils
    ~~~~~~~~~~~~~~

    utils used in wiki app

    :copyright: (c) 2016 by zifeiyu.
    :license: MIT, see LICENSE for more details.
"""
import os

def sphinx_build(script):
    return os.system(script)
