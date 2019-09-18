#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .views import ContactView


class ContactSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return [
            {'view_name': 'contact:index', 'lastmod': ContactView.last_modification},
        ]

    def location(self, item):
        return reverse(item['view_name'])

    def lastmod(self, item):
        return item['lastmod']
