#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from datetime import datetime

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control, cache_page
from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _

from .services import PricingService


@method_decorator(cache_control(max_age=1 * 24 * 60 * 60), name='get')  # 1 day
@method_decorator(cache_page(1 * 24 * 60 * 60), name='get')  # 1 day
class PricingView(TemplateView):
    http_method_names = ['get']
    template_name = 'pricing/pricing.html'
    last_modification = datetime(2019, 12, 2)

    def get_context_data(self, amp=None):
        context = super(PricingView, self).get_context_data(amp=amp)
        context.update({
            'title': _('Pricing | Upkook Startup'),
            'description': _('Cx metrics prices'),
            'nik_url': "https://nikstarter.com/projects/%DA%AF%D8%AC%D8%AA%D9%87%D8%A7%DB%8C-"
                       "%D9%87%D9%88%D8%B4%D9%85%D9%86%D8%AF/%D8%A2%D9%BE-%DA%A9%D9%88%DA%A9"
        })

        if amp == 'amp' or self.request.GET:
            context.update({'canonical_url': PricingService.get_index_absolute_url(self.request, is_amp=False)})
        if amp != 'amp':
            context.update({'amp_url': PricingService.get_index_absolute_url(self.request, is_amp=True)})

        return context
