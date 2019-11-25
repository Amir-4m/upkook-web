#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.test import TestCase
from upkook_web.apps.cms.home.views import CarouselItem


class CarouselItemTestCase(TestCase):

    def test_src_img_set(self):
        carousel_item = CarouselItem(img_src=self.id())
        carousel_item.img_src = 'src'
        self.assertEqual(carousel_item.img_src, 'src')

    def test_src_img2_set(self):
        carousel_item = CarouselItem(img_src=self.id(), img_src2=self.id())
        carousel_item.img_src = 'src'
        carousel_item.img_src2 = 'src2'
        self.assertEqual(carousel_item.img_src, 'src')
        self.assertEqual(carousel_item.img_src2, 'src2')

    def test_alt_set(self):
        carousel_item = CarouselItem(img_src=self.id(), alt=self.id())
        carousel_item.alt = 'test pic'
        self.assertEqual(carousel_item.alt, 'test pic')

    def test_url_set(self):
        carousel_item = CarouselItem(img_src=self.id(), url=self.id())
        carousel_item.url = 'fake'
        self.assertEqual(carousel_item.url, 'fake')

    def test_target_set(self):
        carousel_item = CarouselItem(img_src=self.id(), target=self.id())
        carousel_item.target = '_blank'
        self.assertEqual(carousel_item.target, '_blank')
