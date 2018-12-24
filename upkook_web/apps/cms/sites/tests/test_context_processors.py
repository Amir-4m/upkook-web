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
@override_settings(
    ROOT_URLCONF='upkook_web.apps.cms.sites.tests.urls',
    TEMPLATES=[{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'upkook_web.apps.cms.sites.context_processors.site_settings',
            ],
        },
    }],
    INSTALLED_APPS=(
        'upkook_web.apps.cms.sites',
        'upkook_web.apps.cms.sites.tests',
    )
)
class SiteContextProcessorTestCase(TestCase):
    @override_settings(
        GTM_ID='fake',
        HOSTNAME='www.upkook.com',
        API_URL="/"
    )
    def test_site_settings(self):
        response = self.client.get(reverse('request_site'))
        self.assertEqual(response.context.get('hostname'), 'www.upkook.com')
        self.assertEqual(response.context.get('gtm_id'), 'fake')
        self.assertEqual(response.context.get('api_url'), "/")

    def test_site_settings_none(self):
        response = self.client.get(reverse('request_site'))
        self.assertIsNone(response.context.get('hostname'))
        self.assertIsNone(response.context.get('gtm_id'))
        self.assertIsNone(response.context.get('api_url'))
