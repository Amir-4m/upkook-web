#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.conf.urls import url
from .views import HomeView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='index')
]
