#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.urls import path, include
from . import urlpatterns

urlpatterns += [
    path('', include('upkook_web.apps.cms.home.urls', 'home')),
    path('', include('django_contrib.sites.urls.web', 'sites')),
]
