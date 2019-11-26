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
)

API_URL = get_env_var("API_URL")

DASHBOARD_URL = get_env_var('DASHBOARD_URL', 'https://dash.upkook.com')

AUTH_COOKIE_AGE = get_env_var('AUTH_COOKIE_AGE', 24 * 60 * 60)  # (1 day, in seconds)
AUTH_COOKIE_DOMAIN = get_env_var('AUTH_COOKIE_DOMAIN')
AUTH_COOKIE_SECURE = get_env_var('AUTH_COOKIE_SECURE', False) == 'True'
AUTH_ACCESS_COOKIE_NAME = get_env_var('AUTH_ACCESS_COOKIE_NAME', 'access')
AUTH_REFRESH_COOKIE_NAME = get_env_var('AUTH_REFRESH_COOKIE_NAME', 'refresh')
AUTH_USER_TRACK_ID_COOKIE_NAME = get_env_var('AUTH_USER_TRACK_ID_COOKIE_NAME', 'uti')

DRF_RECAPTCHA_VERIFY_ENDPOINT = "https://www.google.com/recaptcha/api/siteverify"
DRF_RECAPTCHA_PUBLIC_KEY = get_env_var("DRF_RECAPTCHA_PUBLIC_KEY", "6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI")

INTRO_APARAT_VIDEO_SRC = get_env_var("INTRO_APARAT_VIDEO_SRC")
INTRO_APARAT_VIDEO_AMP_SRC = get_env_var("INTRO_APARAT_VIDEO_AMP_SRC")
INTRO_APARAT_VIDEO_ID = get_env_var("INTRO_APARAT_VIDEO_ID")
