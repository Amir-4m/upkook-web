#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .views import VideosView


class VideosSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return [
            {'view_name': 'videos:index', 'lastmod': VideosView.last_modification},
        ]

    def location(self, item):
        return reverse(item['view_name'])

    def lastmod(self, item):
        return item['lastmod']
