#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.conf.urls import url, include
from . import urlpatterns

urlpatterns += [
    url(r'^', include('upkook_web.apps.cms.policies.urls', 'policies')),
]
