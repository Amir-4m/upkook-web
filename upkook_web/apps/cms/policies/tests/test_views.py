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

    def test_get(self):
        url = reverse(self.view_name)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)