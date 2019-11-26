#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
import unittest
import os
from django.test import TestCase
from datetime import datetime

from ..sitemap import VideosSitemap
from django.urls import reverse


class VideosSitemapTestCase(TestCase):
    def setUp(self):
        self.item = VideosSitemap().items()[0]

    def test_changefreq(self):
        sitemap = VideosSitemap()
        self.assertEqual(sitemap.changefreq, 'weekly')

    def test_priority(self):
        sitemap = VideosSitemap()
        self.assertEqual(sitemap.priority, 0.5)

    def test_items(self):
        items = VideosSitemap().items()
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]['view_name'], 'videos:index')
        self.assertEqual(items[0]['lastmod'], datetime(2019, 11, 25))

    def test_lastmod(self):
        last_mod = VideosSitemap().lastmod(self.item)
        self.assertEqual(last_mod, datetime(2019, 11, 25))

    @unittest.skipIf(
        os.environ['DJANGO_SETTINGS_MODULE'] != 'upkook_web.settings.web',
        'This test is intended only for web settings.'
    )
    def test_location(self):
        location = VideosSitemap().location(self.item)
        self.assertEqual(location, reverse('videos:index'))
