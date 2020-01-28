#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from .web_base import *  # NOQA

ROOT_URLCONF = 'upkook_web.urls.web'

INSTALLED_APPS += (
    'upkook_web.apps.cms.home',
    'upkook_web.apps.users',
    'upkook_web.apps.cms.hiw',
    'upkook_web.apps.cms.about',
    'upkook_web.apps.cms.contact',
    'upkook_web.apps.cms.videos',
    'upkook_web.apps.cms.pricing',
    'upkook_web.apps.cms.features',
)

MIDDLEWARE = (
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'django.middleware.common.CommonMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
)

API_URL = get_env_var("API_URL")

AUTH_COOKIE_AGE = get_env_var('AUTH_COOKIE_AGE', 24 * 60 * 60)  # (1 day, in seconds)
AUTH_COOKIE_DOMAIN = get_env_var('AUTH_COOKIE_DOMAIN')
AUTH_COOKIE_SECURE = get_env_var('AUTH_COOKIE_SECURE', False) == 'True'
AUTH_ACCESS_COOKIE_NAME = get_env_var('AUTH_ACCESS_COOKIE_NAME', 'access')
AUTH_REFRESH_COOKIE_NAME = get_env_var('AUTH_REFRESH_COOKIE_NAME', 'refresh')
AUTH_USER_TRACK_ID_COOKIE_NAME = get_env_var('AUTH_USER_TRACK_ID_COOKIE_NAME', 'uti')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Subject-line prefix for email messages sent.
EMAIL_SUBJECT_PREFIX = '[UPKOOK] '

DEFAULT_FROM_EMAIL = 'Upkook <noreply@upkook.com>'

SERVER_EMAIL = 'server@upkook.com'

# The host to use for sending email.
EMAIL_HOST = get_env_var('EMAIL_HOST', 'smtp.mailgun.org')

# Username to use for the SMTP server defined in EMAIL_HOST.
EMAIL_HOST_USER = get_env_var('EMAIL_HOST_USER', '')

# Password to use for the SMTP server defined in EMAIL_HOST.
EMAIL_HOST_PASSWORD = get_env_var('EMAIL_HOST_PASSWORD', '')

# Port to use for the SMTP server defined in EMAIL_HOST.
EMAIL_PORT = get_env_var('EMAIL_PORT', 587)

# Whether to use a TLS (secure) connection when talking to the SMTP server.
EMAIL_USE_TLS = get_env_var('EMAIL_USE_TLS', 'True') == 'True'
