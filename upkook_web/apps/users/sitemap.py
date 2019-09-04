#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .views import SignInView, SignUpView


class UsersSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.6

    def items(self):
        return [
            {'view_name': 'users:sign-in', 'lastmod': SignInView.last_modification},
            {'view_name': 'users:sign-up', 'lastmod': SignUpView.last_modification},
        ]

    def location(self, item):
        return reverse(item['view_name'])

    def lastmod(self, item):
        return item['lastmod']
