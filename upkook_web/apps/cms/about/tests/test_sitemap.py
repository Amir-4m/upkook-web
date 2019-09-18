#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
import unittest
import os
from django.test import TestCase
from datetime import datetime

from ..sitemap import AboutSitemap
from django.urls import reverse


class AboutSitemapTestCase(TestCase):
    def setUp(self):
        self.item = AboutSitemap().items()[0]

    def test_changefreq(self):
        sitemap = AboutSitemap()
        self.assertEqual(sitemap.changefreq, 'weekly')

    def test_priority(self):
        sitemap = AboutSitemap()
        self.assertEqual(sitemap.priority, 0.8)

    def test_items(self):
        items = AboutSitemap().items()
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]['view_name'], 'about:index')
        self.assertEqual(items[0]['lastmod'], datetime(2019, 9, 14))

    def test_lastmod(self):
        last_mod = AboutSitemap().lastmod(self.item)
        self.assertEqual(last_mod, datetime(2019, 9, 14))

    @unittest.skipIf(
        os.environ['DJANGO_SETTINGS_MODULE'] != 'upkook_web.settings.web',
        'This test is intended only for web settings.'
    )
    def test_location(self):
        location = AboutSitemap().location(self.item)
        self.assertEqual(location, reverse('about:index'))
