#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.conf import settings


def upkook_web(request):
    return {'pure_chat_id': settings.PURE_CHAT_ID}
