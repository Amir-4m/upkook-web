#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.test import TestCase
from django.urls import reverse


class HomeViewTestCase(TestCase):
    view_name = 'home:index'

    def test_get(self):
        url = reverse(self.view_name)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
