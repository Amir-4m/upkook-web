#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.utils.translation import ugettext_lazy as _

from .base import *  # NOQA

USE_I18N = True

LANGUAGES = (
    ('en-us', _('English')),
    ('fa', _('Farsi')),
)

TEMPLATES[0]['OPTIONS'] = {
    'debug': DEBUG,
    'context_processors': (
        'django.template.context_processors.i18n',
        'django.template.context_processors.static',
        'django.template.context_processors.request',
        'sekizai.context_processors.sekizai',
        'django_contrib.sites.context_processors.site_settings',
        'django_contrib.amp.context_processors.amp',
        'upkook_web.apps.contrib.api.context_processors.api',
        'upkook_web.context_processors.upkook_web'
    ),
    # List of callables that know how to import templates from
    # various sources.
    'loaders': (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )
}

INSTALLED_APPS += (
    'statici18n',
    'django.contrib.sites',
    'django.contrib.sitemaps',

    'django_contrib.amp',
    'django_contrib.sites',
    'django_contrib.seo',
    'django_contrib.social',
    'django_contrib.chats',
    'upkook_web.apps.contrib.api',

)

PURE_CHAT_ID = get_env_var('PURE_CHAT_ID')

IRAN_YEKAN_LICENSE = get_env_var('IRAN_YEKAN_LICENSE', '3.0')

GA_VERSION = get_env_var('GA_VERSION', 'GA1')

GA_COOKIE_NAME = get_env_var('GA_COOKIE_NAME', '_ga')
GA_COOKIE_AGE = int(get_env_var('GA_COOKIE_AGE', 2 * 365 * 24 * 60 * 60))  # 2 years
GA_COOKIE_PATH = get_env_var('GA_COOKIE_PATH', '/')
GA_COOKIE_DOMAIN = get_env_var('GA_COOKIE_DOMAIN')
GA_COOKIE_SECURE = get_env_var('GA_COOKIE_SECURE', 'False') == 'True'

GTM_AMP_CONF_URL = get_env_var('GTM_AMP_CONF_URL', 'https://www.googletagmanager.com/amp.json')
GTM_CONFIG_CACHE_TIMEOUT = int(get_env_var('GTM_CONFIG_CACHE_TIMEOUT', 10 * 60))  # 10 minutes

AMP_CONFIG_CORS_ORIGIN_WHITELIST = [i for i in get_env_var('AMP_CONFIG_CORS_ORIGIN_WHITELIST', "").split(",") if i]
