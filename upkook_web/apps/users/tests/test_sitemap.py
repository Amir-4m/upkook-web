#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
import unittest
import os
from django.test import TestCase
from datetime import datetime

from ..sitemap import UsersSitemap
from django.urls import reverse


class UserSitemapTestCase(TestCase):
    def setUp(self):
        self.item = UsersSitemap().items()[0]

    def test_changefreq(self):
        sitemap = UsersSitemap()
        self.assertEqual(sitemap.changefreq, 'weekly')

    def test_priority(self):
        sitemap = UsersSitemap()
        self.assertEqual(sitemap.priority, 0.6)

    def test_items(self):
        items = UsersSitemap().items()
        self.assertEqual(len(items), 2)
        self.assertEqual(items[0]['view_name'], 'users:sign-in')
        self.assertEqual(items[0]['lastmod'], datetime(2019, 8, 26))

    def test_lastmod(self):
        last_mod = UsersSitemap().lastmod(self.item)
        self.assertEqual(last_mod, datetime(2019, 8, 26))

    @unittest.skipIf(
        os.environ['DJANGO_SETTINGS_MODULE'] != 'upkook_web.settings.web',
        'This test is intended only for web settings.'
    )
    def test_location(self):
        location = UsersSitemap().location(self.item)
        self.assertEqual(location, reverse('users:sign-in'))
