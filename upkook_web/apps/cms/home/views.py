#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control, cache_page
from django.views.generic import TemplateView
from django_contrib.sites.services import SiteService
from django.conf import settings

from .services import HomeService
from upkook_web.apps.cms.showcase.showcase_item import ShowcaseItem


@method_decorator(cache_control(max_age=1 * 24 * 60 * 60), name='get')  # 1 day
@method_decorator(cache_page(1 * 24 * 60 * 60), name='get')  # 1 day
class HomeView(TemplateView):
    http_method_names = ['get']
    template_name = 'home/index.html'

    def get_context_data(self, amp=None):
        context = super(HomeView, self).get_context_data(amp=amp)
        site = SiteService.get_current_site(self.request)
        context.update({'title': site.name})
        img_src1 = '%s%s' % (settings.STATIC_URL, 'home/images/huawei.png')
        img_src2 = '%s%s' % (settings.STATIC_URL, 'home/images/honda.png')
        img_src3 = '%s%s' % (settings.STATIC_URL, 'home/images/apple.png')
        img_src4 = '%s%s' % (settings.STATIC_URL, 'home/images/google.png')
        img_src5 = '%s%s' % (settings.STATIC_URL, 'home/images/amazon.png')
        img_src6 = '%s%s' % (settings.STATIC_URL, 'home/images/airbnb.png')
        img_src7 = '%s%s' % (settings.STATIC_URL, 'home/images/microsoft.png')
        img_src8 = '%s%s' % (settings.STATIC_URL, 'home/images/netflix.png')

        context.update({
            'showcase_items': [
                ShowcaseItem(img_src=img_src1),
                ShowcaseItem(img_src=img_src2),
                ShowcaseItem(img_src=img_src3),
                ShowcaseItem(img_src=img_src4),
                ShowcaseItem(img_src=img_src5),
                ShowcaseItem(img_src=img_src6),
                ShowcaseItem(img_src=img_src7),
                ShowcaseItem(img_src=img_src8),
            ]
        })
        if amp == 'amp':
            context.update({'canonical_url': HomeService.get_index_absolute_url(self.request, is_amp=False)})
        else:
            context.update({'amp_url': HomeService.get_index_absolute_url(self.request, is_amp=True)})

        return context
