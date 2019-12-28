#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
import unittest
import os
from django.test import TestCase
from datetime import datetime

from ..sitemap import FeaturesSitemap
from django.urls import reverse


class FeaturesSitemapTestCase(TestCase):
    def setUp(self):
        self.item = FeaturesSitemap().items()[0]

    def test_changefreq(self):
        sitemap = FeaturesSitemap()
        self.assertEqual(sitemap.changefreq, 'weekly')

    def test_priority(self):
        sitemap = FeaturesSitemap()
        self.assertEqual(sitemap.priority, 0.7)

    def test_items(self):
        items = FeaturesSitemap().items()
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]['view_name'], 'features:index')
        self.assertEqual(items[0]['lastmod'], datetime(2019, 12, 28))

    def test_lastmod(self):
        last_mod = FeaturesSitemap().lastmod(self.item)
        self.assertEqual(last_mod, datetime(2019, 12, 28))

    @unittest.skipIf(
        os.environ['DJANGO_SETTINGS_MODULE'] != 'upkook_web.settings.web',
        'This test is intended only for web settings.'
    )
    def test_location(self):
        location = FeaturesSitemap().location(self.item)
        self.assertEqual(location, reverse("features:index"))
