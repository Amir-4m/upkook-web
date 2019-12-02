#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.utils.translation import ugettext_lazy as _

from .base import *  # NOQA

USE_I18N = True

LANGUAGES = (
    ('en-us', _('English')),
    ('fa', _('Farsi')),
)

INSTALLED_APPS += (
    'statici18n',
    'django.contrib.sites',
    'django_contrib.sites',
    'django_contrib.social',
    'django_contrib.lazy',
    'upkook_web.apps.contrib.api',
    'upkook_web.apps.cms.home',
    'upkook_web.apps.cms.hiw',
    'upkook_web.apps.users',
    'upkook_web.apps.cms.policies',
    'upkook_web.apps.cms.about',
    'upkook_web.apps.cms.contact',
    'upkook_web.apps.cms.videos',
    'upkook_web.apps.cms.pricing',

)
INTRO_APARAT_VIDEO_SRC = get_env_var("INTRO_APARAT_VIDEO_SRC")
INTRO_APARAT_VIDEO_AMP_SRC = get_env_var("INTRO_APARAT_VIDEO_AMP_SRC")
INTRO_APARAT_VIDEO_ID = get_env_var("INTRO_APARAT_VIDEO_ID")
