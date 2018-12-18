#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from .base import *  # NOQA

INSTALLED_APPS += (
    'upkook_web.apps.cms.sites',
    'upkook_web.apps.cms.home',
    'upkook_web.apps.customers',
    'upkook_web.apps.cms.policies',
)

HOSTNAME = get_env_var("HOSTNAME")

GTM_ID = get_env_var("GTM_ID")
