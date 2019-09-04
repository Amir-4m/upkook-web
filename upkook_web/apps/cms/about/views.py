#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control, cache_page
from django.views.generic import TemplateView
from datetime import datetime
from django.utils.translation import gettext_lazy as _
from .services import AboutService


@method_decorator(cache_control(max_age=1 * 24 * 60 * 60), name='get')  # 1 day
@method_decorator(cache_page(1 * 24 * 60 * 60), name='get')  # 1 day
class AboutView(TemplateView):
    http_method_names = ['get']
    template_name = 'about/about-us.html'
    last_modification = datetime(2019, 8, 26)

    def get_context_data(self, amp=None):
        context = super(AboutView, self).get_context_data(amp=amp)
        context.update({
            'title': 'about us',
            'description': 'about us description'
        })

        if amp == 'amp' or self.request.GET:
            context.update({'canonical_url': AboutService.get_index_absolute_url(self.request, is_amp=False)})
        if amp != 'amp':
            context.update({'amp_url': AboutService.get_index_absolute_url(self.request, is_amp=True)})

        return context
