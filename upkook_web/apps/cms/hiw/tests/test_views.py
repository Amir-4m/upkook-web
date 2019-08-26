#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
import os
import unittest
from django.test import TestCase, override_settings
from django.urls import reverse


@unittest.skipIf(
    os.environ['DJANGO_SETTINGS_MODULE'] != 'upkook_web.settings.web',
    'This test is intended only for web settings.'
)
class HIWViewTestCase(TestCase):
    fixtures = ['sites']
    view_name = 'hiw:hiw'
    amp_view_name = 'hiw:hiw-amp'

    @override_settings(
        DASHBOARD_URL='https://testserver/dashboard/',
        AUTH_COOKIE_AGE=1,
        AUTH_COOKIE_DOMAIN='testserver',
        AUTH_COOKIE_PATH='/',
        AUTH_COOKIE_SECURE='True',
        AUTH_ACCESS_COOKIE_NAME='access',
        AUTH_REFRESH_COOKIE_NAME='refresh',
        AUTH_USER_TRACK_ID_COOKIE_NAME='uti',
    )
    def test_get(self):
        url = reverse(self.view_name)
        response = self.client.get(url)

        auth_cookie = response.context_data.get('auth_cookie')
        self.assertEqual(auth_cookie.get('age'), 1)
        self.assertEqual(auth_cookie.get('domain'), 'testserver')
        self.assertEqual(auth_cookie.get('path'), '/')
        self.assertTrue(auth_cookie.get('secure'))
        self.assertEqual(auth_cookie.get('access_key'), 'access')
        self.assertEqual(auth_cookie.get('refresh_key'), 'refresh')
        self.assertEqual(auth_cookie.get('user_track_id_key'), 'uti')
        self.assertEqual(response.context_data.get('title'), 'How It Works')
        self.assertEqual(response.context_data.get('amp_url'), 'http://testserver/how-it-works/amp/')
        self.assertEqual(response.status_code, 200)

    def test_get_amp(self):
        url = reverse(self.amp_view_name, kwargs={'amp': 'amp'})
        response = self.client.get(url)
        self.assertEqual(response.context_data.get('canonical_url'), 'http://testserver/how-it-works/')
        self.assertEqual(response.status_code, 200)
