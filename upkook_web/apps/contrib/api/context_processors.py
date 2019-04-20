#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.conf import settings


def api(request):
    return {'api_url': settings.API_URL}
