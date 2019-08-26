#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control, cache_page
from django.views.generic import TemplateView
from django_contrib.sites.services import SiteService
from django.conf import settings
from django.utils.translation import gettext_lazy as _


from .services import HomeService
from upkook_web.apps.cms.showcase.showcase_item import ShowcaseItem
from django_contrib.html.link import Link


@method_decorator(cache_control(max_age=1 * 24 * 60 * 60), name='get')  # 1 day
@method_decorator(cache_page(1 * 24 * 60 * 60), name='get')  # 1 day
class HomeView(TemplateView):
    http_method_names = ['get']
    template_name = 'home/index.html'

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
            'promo_box_cta': Link(text=_('Free sign up'), href=reverse('users:sign-up')),
        })

        return context
