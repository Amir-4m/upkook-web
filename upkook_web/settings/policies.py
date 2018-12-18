#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from .web_base import *  # NOQA

ROOT_URLCONF = 'upkook_web.urls.policies'

INSTALLED_APPS += (
    'upkook_web.apps.cms.policies',
)
