#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.conf.urls import url
from .views import request_site

urlpatterns = [
    url(r'^request_site/$', request_site, name='request_site'),
]
