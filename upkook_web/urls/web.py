#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.urls import path, include
from . import urlpatterns

urlpatterns += [
    path('', include('upkook_web.apps.cms.home.urls', 'home')),
    path('', include('django_contrib.sites.urls.web', 'sites')),
    path('', include('upkook_web.apps.users.urls', 'users')),
    path('', include('upkook_web.apps.cms.hiw.urls', 'hiw'))
]
