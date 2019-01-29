#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView
from django_contrib.sites.services import SiteService

from .services import HomeService


class HomeView(TemplateView):
    http_method_names = ['get']
    template_name = 'home/index.html'

    def get_context_data(self, amp=None):
        context = super(HomeView, self).get_context_data(amp=amp)
        site = SiteService.get_current_site(self.request)
        context.update({'title': site.name})
        if amp == 'amp':
            context.update({'canonical_url': HomeService.get_index_absolute_url(self.request, is_amp=False)})
        else:
            context.update({'amp_url': HomeService.get_index_absolute_url(self.request, is_amp=True)})

        return context

    @method_decorator(cache_page(1 * 24 * 60 * 60))  # 1 day
    def get(self, request, *args, **kwargs):
        return super(HomeView, self).get(request, *args, **kwargs)
