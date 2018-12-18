#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class TermsView(TemplateView):
    http_method_names = ['get']
    template_name = 'policies/terms.html'

    @method_decorator(cache_page(1 * 24 * 60 * 60))  # 1 day
    def get(self, request, *args, **kwargs):
        return super(TermsView, self).get(request, *args, **kwargs)
