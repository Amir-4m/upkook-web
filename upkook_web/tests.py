#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.core.handlers.wsgi import WSGIHandler
from django.test import TestCase

from .wsgi import application


class WSGITestCase(TestCase):
    def test_application(self):
        self.assertIsInstance(application, WSGIHandler)
