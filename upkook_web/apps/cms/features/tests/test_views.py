#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
import os
import unittest
from django.test import TestCase
from django.urls import reverse


@unittest.skipIf(
    os.environ['DJANGO_SETTINGS_MODULE'] != 'upkook_web.settings.web',
    'This test is intended only for web settings.'
)
class FeaturesViewTestCase(TestCase):
    fixtures = ['sites']
    view_name = 'features:index'
    amp_view_name = 'features:index-amp'

    def test_get(self):
        url = reverse(self.view_name)
        response = self.client.get(url)

        self.assertEqual(
            response.context_data.get('title'),
            'Features | Upkook Startup'
        )
        self.assertEqual(response.context_data.get('amp_url'), 'http://testserver/features/amp/')
        self.assertEqual(response.status_code, 200)

    def test_get_amp(self):
        url = reverse(self.amp_view_name, kwargs={'amp': 'amp'})
        response = self.client.get(url)
        self.assertEqual(response.context_data.get('canonical_url'), 'http://testserver/features/')
        self.assertEqual(response.status_code, 200)
