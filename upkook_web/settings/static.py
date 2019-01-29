#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from .base import *  # NOQA

INSTALLED_APPS += (
    'django.contrib.sites',
    'django_contrib.sites',
    'upkook_web.apps.cms.home',
    'upkook_web.apps.customers',
    'upkook_web.apps.cms.policies',
)
