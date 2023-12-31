#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
import unittest

import os
from django.test import TestCase, override_settings
from django.urls import reverse


@unittest.skipIf(
    os.environ['DJANGO_SETTINGS_MODULE'] != 'upkook_web.settings.web',
    'This test is intended only for web settings.'
)
class SignInViewTestCase(TestCase):
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
        url = reverse('users:sign-in')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        context = response.context_data

        self.assertEqual(context.get('title'), "Welcome, log in to UPKOOK - UPKOOK")
        self.assertEqual(context.get('dashboard_url'), 'https://testserver/dashboard/')
        self.assertEqual(context.get('sign_up_url'), reverse('users:sign-up'))
        self.assertEqual(context.get('forgot_password_url'), reverse('users:forgot-password'))

        auth_cookie = context.get('auth_cookie')
        self.assertEqual(auth_cookie.get('age'), 1)
        self.assertEqual(auth_cookie.get('domain'), 'testserver')
        self.assertEqual(auth_cookie.get('path'), '/')
        self.assertTrue(auth_cookie.get('secure'))
        self.assertEqual(auth_cookie.get('access_key'), 'access')
        self.assertEqual(auth_cookie.get('refresh_key'), 'refresh')
        self.assertEqual(auth_cookie.get('user_track_id_key'), 'uti')


@unittest.skipIf(
    os.environ['DJANGO_SETTINGS_MODULE'] != 'upkook_web.settings.web',
    'This test is intended only for web settings.'
)
class ForgotPasswordTestCase(TestCase):
    def test_get(self):
        url = reverse('users:forgot-password')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        context = response.context_data

        self.assertEqual(context.get('title'), "Forgot Password - UPKOOK")
        self.assertEqual(context.get('sign_up_url'), reverse('users:sign-up'))
        self.assertEqual(context.get('sign_in_url'), reverse('users:sign-in'))


@unittest.skipIf(
    os.environ['DJANGO_SETTINGS_MODULE'] != 'upkook_web.settings.web',
    'This test is intended only for web settings.'
)
class SignUpViewTestCase(TestCase):
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
        url = reverse('users:sign-up')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        context = response.context_data

        self.assertEqual(context.get('title'), "Free registration in UPKOOK - UPKOOK")
        self.assertEqual(context.get('dashboard_url'), 'https://testserver/dashboard/')

        auth_cookie = context.get('auth_cookie')
        self.assertEqual(auth_cookie.get('age'), 1)
        self.assertEqual(auth_cookie.get('domain'), 'testserver')
        self.assertEqual(auth_cookie.get('path'), '/')
        self.assertTrue(auth_cookie.get('secure'))
        self.assertEqual(auth_cookie.get('access_key'), 'access')
        self.assertEqual(auth_cookie.get('refresh_key'), 'refresh')
        self.assertEqual(auth_cookie.get('user_track_id_key'), 'uti')


@unittest.skipIf(
    os.environ['DJANGO_SETTINGS_MODULE'] != 'upkook_web.settings.web',
    'This test is intended only for web settings.'
)
class ResetPasswordTestCase(TestCase):
    def test_get(self):
        token = "gAAAAABdvtEiROwTmT6PC19QTc29CqCF4naCdPsKcUPPb8hR21Zd3Y9r0Qh-Zb_fwkfGQjlGgRKRk0cTwfPbmsHLKKAe6jwm"
        url = reverse('users:reset-password', kwargs={'token': token})

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        context = response.context_data

        self.assertEqual(context.get('title'), "Reset Password - UPKOOK")
        self.assertEqual(context.get('forgot_password_url'), reverse('users:forgot-password'))
