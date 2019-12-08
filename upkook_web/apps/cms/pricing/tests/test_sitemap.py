#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
import unittest
import os
from django.test import TestCase
from datetime import datetime

from ..sitemap import PricingSitemap
from django.urls import reverse


class AboutSitemapTestCase(TestCase):
    def setUp(self):
        self.item = PricingSitemap().items()[0]

    def test_changefreq(self):
        sitemap = PricingSitemap()
        self.assertEqual(sitemap.changefreq, 'weekly')

    def test_priority(self):
        sitemap = PricingSitemap()
        self.assertEqual(sitemap.priority, 0.8)

    def test_items(self):
        items = PricingSitemap().items()
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]['view_name'], 'pricing:index')
        self.assertEqual(items[0]['lastmod'], datetime(2019, 12, 2))

    def test_lastmod(self):
        last_mod = PricingSitemap().lastmod(self.item)
        self.assertEqual(last_mod, datetime(2019, 12, 2))

    @unittest.skipIf(
        os.environ['DJANGO_SETTINGS_MODULE'] != 'upkook_web.settings.web',
        'This test is intended only for web settings.'
    )
    def test_location(self):
        location = PricingSitemap().location(self.item)
        self.assertEqual(location, reverse('pricing:index'))
