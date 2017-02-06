#/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    zifeiyu.middleware
    ~~~~~~~~~~~~~~

    middleware for whole site

    :copyright: (c) 2016 by zifeiyu.
    :license: MIT, see LICENSE_FILE for more details.
"""
import pytz

from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin


class TimezoneMiddleware(MiddlewareMixin):
    def process_request(self, request):
        timezone.activate(pytz.timezone('Asia/Shanghai'))
