#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
import unittest
import os
from django.test import TestCase
from datetime import datetime

from ..sitemap import HIWSitemap
from django.urls import reverse


class HomeSitemapTestCase(TestCase):
    def setUp(self):
        self.item = HIWSitemap().items()[0]

    def test_changefreq(self):
        sitemap = HIWSitemap()
        self.assertEqual(sitemap.changefreq, 'weekly')

    def test_priority(self):
        sitemap = HIWSitemap()
        self.assertEqual(sitemap.priority, 0.7)

    def test_items(self):
        items = HIWSitemap().items()
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]['view_name'], 'hiw:index')
        self.assertEqual(items[0]['lastmod'], datetime(2019, 8, 26))

    def test_lastmod(self):
        last_mod = HIWSitemap().lastmod(self.item)
        self.assertEqual(last_mod, datetime(2019, 8, 26))

    @unittest.skipIf(
        os.environ['DJANGO_SETTINGS_MODULE'] != 'upkook_web.settings.web',
        'This test is intended only for web settings.'
    )
    def test_location(self):
        location = HIWSitemap().location(self.item)
        self.assertEqual(location, reverse('hiw:index'))
