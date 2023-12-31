#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.urls import reverse
from django.utils.decorators import method_decorator
from datetime import datetime
from django.views.decorators.cache import cache_control, cache_page
from django.views.generic import TemplateView
from django_contrib.sites.services import SiteService
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from .services import HomeService
from upkook_web.apps.cms.showcase.showcase_item import ShowcaseItem
from upkook_web.apps.cms.carousel.carousel_item import CarouselItem
from django_contrib.html.link import Link

nps_intro = {
    "large_img": "%shome/images/nps.png" % settings.STATIC_URL,
    "large_img_alt": _("NPS"),
    "title": _("Product NPS Title"),
    "primary_desc": _("Product NPS Primary Desc"),
    "quote": _("Product NPS Quote"),
    "quote_title": _("Product NPS Quote Title"),
    "list_title": _("Product NPS List Title"),
    "list": [
        _("Product NPS List Item 1"),
        _("Product NPS List Item 2"),
        _("Product NPS List Item 3"),
        _("Product NPS List Item 4"),
        _("Product NPS List Item 5"),
        _("Product NPS List Item 6"),
    ],
    "box_img": "%shome/images/nps-small.png" % settings.STATIC_URL,
    "box_img_alt": _("NPS"),
    "box_desc": _("Product NPS Box Desc ")
}

ces_intro = {
    "large_img": "%shome/images/ces.png" % settings.STATIC_URL,
    "large_img_alt": _("CES"),
    "title": _("Product CES Title"),
    "primary_desc": _("Product CES Primary Desc"),
    "quote": _("Product CES Quote"),
    "quote_title": _("Product CES Quote Title"),
    "list_title": _("Product CES List Title"),
    "list": [
        _("Product CES List Item 1"),
        _("Product CES List Item 2"),
        _("Product CES List Item 3"),
        _("Product CES List Item 4"),
        _("Product CES List Item 5"),
        _("Product CES List Item 6"),
    ],
    "box_img": "%shome/images/ces-small.png" % settings.STATIC_URL,
    "box_img_alt": _("CES"),
    "box_desc": _("Product CES Box Desc ")
}

csat_intro = {
    "large_img": "%shome/images/csat.png" % settings.STATIC_URL,
    "large_img_alt": _("CSAT"),
    "title": _("Product CSAT Title"),
    "primary_desc": _("Product CSAT Primary Desc"),
    "quote": _("Product CSAT Quote"),
    "quote_title": _("Product CSAT Quote Title"),
    "list_title": _("Product CSAT List Title"),
    "list": [
        _("Product CSAT List Item 1"),
        _("Product CSAT List Item 2"),
        _("Product CSAT List Item 3"),
        _("Product CSAT List Item 4"),
        _("Product CSAT List Item 5"),
        _("Product CSAT List Item 6"),
    ],
    "box_img": "%shome/images/csat-small.png" % settings.STATIC_URL,
    "box_img_alt": _("CSAT"),
    "box_desc": _("Product CSAT Box Desc ")
}


@method_decorator(cache_control(max_age=1 * 24 * 60 * 60), name='get')  # 1 day
@method_decorator(cache_page(1 * 24 * 60 * 60), name='get')  # 1 day
class HomeView(TemplateView):
    http_method_names = ['get']
    template_name = 'home/index.html'
    last_modification = datetime(2019, 8, 26)

    def get_context_data(self, amp=None):
        context = super(HomeView, self).get_context_data(amp=amp)
        site = SiteService.get_current_site(self.request)
        context.update({'title': site.name})

        if amp == 'amp' or self.request.GET:
            context.update({'canonical_url': HomeService.get_index_absolute_url(self.request, is_amp=False)})
        if amp != 'amp':
            context.update({'amp_url': HomeService.get_index_absolute_url(self.request, is_amp=True)})

        context.update({
            'showcase_items': [
                ShowcaseItem(img_src='%s%s' % (settings.STATIC_URL, 'home/images/huawei.png')),
                ShowcaseItem(img_src='%s%s' % (settings.STATIC_URL, 'home/images/honda.png')),
                ShowcaseItem(img_src='%s%s' % (settings.STATIC_URL, 'home/images/apple.png')),
                ShowcaseItem(img_src='%s%s' % (settings.STATIC_URL, 'home/images/google.png')),
                ShowcaseItem(img_src='%s%s' % (settings.STATIC_URL, 'home/images/amazon.png')),
                ShowcaseItem(img_src='%s%s' % (settings.STATIC_URL, 'home/images/airbnb.png')),
                ShowcaseItem(img_src='%s%s' % (settings.STATIC_URL, 'home/images/microsoft.png')),
                ShowcaseItem(img_src='%s%s' % (settings.STATIC_URL, 'home/images/netflix.png')),
            ],
            'carousel_items': [
                CarouselItem(
                    img_src='%s%s' % (settings.STATIC_URL, 'home/images/survey.png'),
                    img_src2='%s%s' % (settings.STATIC_URL, 'home/images/survey-sm.png'),
                    description=_('Make your custom survey.'),
                ),
                CarouselItem(
                    img_src='%s%s' % (settings.STATIC_URL, 'home/images/message.png'),
                    img_src2='%s%s' % (settings.STATIC_URL, 'home/images/message-sm.png'),
                    description=_('Set your custom settings.'),
                ),
                CarouselItem(
                    img_src='%s%s' % (settings.STATIC_URL, 'home/images/final-review.png'),
                    img_src2='%s%s' % (settings.STATIC_URL, 'home/images/final-review-sm.png'),
                    description=_('Make your survey complete.'),
                ),
                CarouselItem(
                    img_src='%s%s' % (settings.STATIC_URL, 'home/images/share-link.png'),
                    img_src2='%s%s' % (settings.STATIC_URL, 'home/images/share-link-sm.png'),
                    description=_('Tell your customers.'),
                ),
                CarouselItem(
                    img_src='%s%s' % (settings.STATIC_URL, 'home/images/report.png'),
                    img_src2='%s%s' % (settings.STATIC_URL, 'home/images/report-sm.png'),
                    description=_('See a preview of your survey'),
                ),
            ],
            'promo_box_cta': Link(text=_('Free sign up'), href=reverse('users:sign-up')),
            'nps_intro': nps_intro,
            'ces_intro': ces_intro,
            'csat_intro': csat_intro,

        })

        return context
