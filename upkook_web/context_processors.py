#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.conf import settings


def upkook_web(request):
    return {
        'IRAN_YEKAN_LICENSE': getattr(settings, 'IRAN_YEKAN_LICENSE'),
        'pure_chat_id': settings.PURE_CHAT_ID,
        'recaptcha_public_key': settings.DRF_RECAPTCHA_PUBLIC_KEY,
        'dashboard_url': settings.DASHBOARD_URL
    }
