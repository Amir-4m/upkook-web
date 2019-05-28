#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
import os
import unittest
from django.test import TestCase
from django.urls import reverse


@unittest.skipIf(
    os.environ['DJANGO_SETTINGS_MODULE'] != 'upkook_web.settings.policies',
    'This test is intended only for policies settings.'
)
class TermsViewTestCase(TestCase):
    view_name = "policies:terms"
    amp_view_name = "policies:terms-amp"

    def test_get(self):
        url = reverse(self.view_name)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_get_amp(self):
        url = reverse(self.amp_view_name, kwargs={'amp': 'amp'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


@unittest.skipIf(
    os.environ['DJANGO_SETTINGS_MODULE'] != 'upkook_web.settings.policies',
    'This test is intended only for policies settings.'
)
class IndexViewTestCase(TestCase):
    view_name = "policies:index"

    def test_get(self):
        url = reverse(self.view_name)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


@unittest.skipIf(
    os.environ['DJANGO_SETTINGS_MODULE'] != 'upkook_web.settings.policies',
    'This test is intended only for policies settings.'
)
class PrivacyViewTestCase(TestCase):
    view_name = "policies:privacy"

    def test_get(self):
        url = reverse(self.view_name)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
