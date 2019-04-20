#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.test import TestCase, override_settings
from django.urls import reverse


@override_settings(
    ROOT_URLCONF='upkook_web.apps.contrib.api.tests.urls',
    TEMPLATES=[{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'upkook_web.apps.contrib.api.context_processors.api',
            ],
        },
    }],
    INSTALLED_APPS=(
        'upkook_web.apps.contrib.api',
        'upkook_web.apps.contrib.api.tests',
    ),
)
class APIContextProcessorTestCase(TestCase):
    @override_settings(API_URL='https://testserver/api/')
    def test_api_url(self):
        response = self.client.get(reverse('site'))
        api_url = response.context.get('api_url')
        self.assertEqual(api_url, 'https://testserver/api/')
