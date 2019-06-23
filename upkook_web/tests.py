#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
import unittest
import os

from django.conf import settings
from django.core.handlers.wsgi import WSGIHandler
from django.test import TestCase

from .context_processors import upkook_web
from .wsgi import application


class WSGITestCase(TestCase):
    def test_application(self):
        self.assertIsInstance(application, WSGIHandler)


@unittest.skipIf(
    os.environ['DJANGO_SETTINGS_MODULE'] != 'upkook_web.settings.web',
    'This test is intended only for web settings.'
)
class UpkookWebContextProcessorTestCase(TestCase):

    def test_upkook_web(self):
        context = upkook_web('')
        self.assertEqual(context['pure_chat_id'], settings.PURE_CHAT_ID)
