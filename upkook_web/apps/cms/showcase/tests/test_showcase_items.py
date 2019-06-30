#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.test import TestCase
from upkook_web.apps.cms.home.views import ShowcaseItem


class ShowcaseItemTestCase(TestCase):

    def test_src_img_set(self):
        showcase_item = ShowcaseItem(img_src=self.id())
        showcase_item.img_src = 'src'
        self.assertEqual(showcase_item.img_src, 'src')

    def test_alt_set(self):
        showcase_item = ShowcaseItem(img_src=self.id(), alt=self.id())
        showcase_item.alt = 'test pic'
        self.assertEqual(showcase_item.alt, 'test pic')

    def test_url_set(self):
        showcase_item = ShowcaseItem(img_src=self.id(), url=self.id())
        showcase_item.url = 'fake'
        self.assertEqual(showcase_item.url, 'fake')

    def test_title_set(self):
        showcase_item = ShowcaseItem(img_src=self.id(), title=self.id())
        showcase_item.title = 'test title'
        self.assertEqual(showcase_item.title, 'test title')

    def test_target_set(self):
        showcase_item = ShowcaseItem(img_src=self.id(), target=self.id())
        showcase_item.target = '_blank'
        self.assertEqual(showcase_item.target, '_blank')
