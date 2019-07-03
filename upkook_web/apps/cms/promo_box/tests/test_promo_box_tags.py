#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.test import TestCase
from django.template import Context, Template
from upkook_web.apps.cms.home.views import Link


class PromoBoxTestCase(TestCase):
    def test_promo_box_full_field(self):
        promo_box_button = Link(
            text='some test text',
            href='/sign-up/',
            target='_blank',
        )
        context = Context({
            'title': 'test title',
            'desc': 'test desc',
            'button': [promo_box_button]
        })
        template = Template('{% load promo_box_tags %} {% promo_box title desc button %}')

        html = template.render(context)

        expected_html = (
            '<div class="promo-wrapper">'

            '<div class="promo-details">'

            '<div class="promo-title">'
            '<h3> test title </h3>'
            '</div>'
            '<div class ="promo-description">'
            '<span> test desc </span>'
            '</div>'
            '<div class="promo-button">'
            '<a href = "/sign-up/" class ="button-cta button-action-primary button-cta-md" '
            'target="_blank">'
            'some test text'
            '</a>'
            '</div>'
            '</div>'
            '</div>'
        )
        print(html)
        print(expected_html)

        self.assertHTMLEqual(html, expected_html)

    def test_promo_box_without_target(self):
        promo_box_button = Link(
            href='/sign-up/',
            text='some test text',
        )
        context = Context({
            'title': 'test title',
            'desc': 'test desc',
            'button': [promo_box_button]
        })
        template = Template('{% load promo_box_tags %} {% promo_box title desc button %}')

        html = template.render(context)

        expected_html = (
            '<div class="promo-wrapper">'
            '<div class="promo-details">'
            '<div class="promo-title">'
            '<h3> test title </h3>'
            '</div>'
            '<div class ="promo-description">'
            '<span> test desc </span>'
            '</div>'
            '<div class="promo-button">'
            '<a href="/sign-up/" class ="button-cta button-action-primary button-cta-md">'
            'some test text'
            '</a>'
            '</div>'
            '</div>'
            '</div>'
        )
        print(html)
        print(expected_html)

        self.assertHTMLEqual(html, expected_html)
