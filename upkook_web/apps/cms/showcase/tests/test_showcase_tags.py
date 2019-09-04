#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.test import TestCase
from django.template import Context, Template
from upkook_web.apps.cms.home.views import ShowcaseItem


class ShowcaseTestCase(TestCase):
    def test_showcase_with_url(self):
        showcase_item = ShowcaseItem(
            img_src='/static/home/images/huawei.png',
            alt='first pic',
            url='https://npsbenchmarks.com/companies/huawei',
            target='_blank'
        )
        context = Context({
            'title': 'test title',
            'desc': 'test desc',
            'items': [showcase_item]
        })
        template = Template('{% load showcase_tags %}{% showcase title desc items %}')

        html = template.render(context)

        expected_html = (
            '<div class="showcase-wrapper mdl-typography--text-center">'
            '<div class="showcase-title">'
            '<h4>test title</h4>'
            'test desc'
            '</div>'
            '<div class="md-gr">'
            '<div class=" md-cl md-cl--3-col  md-cl--2-col-tablet  md-cl--2-col-phone showcase-item">'
            '<a href="https://npsbenchmarks.com/companies/huawei" target="_blank"> '
            '<img src="/static/home/images/huawei.png" alt="first pic" />'
            '</a>'
            '</div>'
            '</div>'
            '</div>'

        )

        self.assertHTMLEqual(html, expected_html)

    def test_showcase_without_url(self):
        showcase_item = ShowcaseItem(
            img_src='/static/home/images/huawei.png',
        )
        context = Context({
            'title': 'test title',
            'desc': 'test desc',
            'items': [showcase_item]
        })
        template = Template('{% load showcase_tags %}{% showcase title desc items %}')

        html = template.render(context)

        expected_html = (
            '<div class="showcase-wrapper mdl-typography--text-center">'
            '<div class="showcase-title">'
            '<h4>test title</h4>'
            'test desc'
            '</div>'
            '<div class="md-gr">'
            '<div class=" md-cl md-cl--3-col  md-cl--2-col-tablet  md-cl--2-col-phone showcase-item">'
            '<img src="/static/home/images/huawei.png" />'
            '</div>'
            '</div>'
            '</div>'

        )
        self.assertHTMLEqual(html, expected_html)
