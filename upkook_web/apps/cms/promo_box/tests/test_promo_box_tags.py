#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.test import TestCase
from django.template import Context, Template
from upkook_web.apps.cms.home.views import Link


class PromoBoxTestCase(TestCase):
    def test_promo_box_full_field(self):
        context = Context({
            'title': 'test title',
            'desc': 'test desc',
            'button': Link(
                text='some test text',
                href='/sign-up/',
                target='_blank',
            )
        })
        template = Template('{% load promo_box_tags %} {% promo_box title desc button %}')

        html = template.render(context)

        expected_html = (
            '<div class="promo-wrapper">'
            '<h3 class="promo-title">test title</h3>'
            '<div class="promo-description">'
            'test desc'
            '</div>'
            '<a href="/sign-up/" class="promo-button button-cta button-action-primary button-cta-md" '
            'target="_blank">'
            'some test text'
            '</a>'
            '</div>'
        )
        self.assertHTMLEqual(html, expected_html)

    def test_promo_box_without_target(self):
        context = Context({
            'title': 'test title',
            'desc': 'test desc',
            'button': Link(
                href='/sign-up/',
                text='some test text',
            )
        })
        template = Template('{% load promo_box_tags %} {% promo_box title desc button %}')

        html = template.render(context)

        expected_html = (
            '<div class="promo-wrapper">'
            '<h3 class="promo-title">test title</h3>'
            '<div class="promo-description">'
            'test desc'
            '</div>'
            '<a href="/sign-up/" class="promo-button button-cta button-action-primary button-cta-md">'
            'some test text'
            '</a>'
            '</div>'
        )
        self.assertHTMLEqual(html, expected_html)
