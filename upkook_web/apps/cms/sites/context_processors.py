#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.conf import settings


def site_settings(request):
    protocol = 'https' if request.is_secure() else 'http'
    return {
        'protocol': protocol, 'hostname': settings.HOSTNAME,
        'gtm_id': settings.GTM_ID, 'api_url': settings.API_URL,
    }
