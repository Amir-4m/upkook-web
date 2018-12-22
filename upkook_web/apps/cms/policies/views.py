#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.utils.translation import ugettext_lazy as _


class TermsView(TemplateView):
    http_method_names = ['get']
    template_name = 'policies/terms.html'

    def get_context_data(self, **kwargs):
        kwargs.update({'title': _('Upkook Terms of Service – Privacy &amp; Terms – Upkook')})
        return super(TermsView, self).get_context_data(**kwargs)

    @method_decorator(cache_page(1 * 24 * 60 * 60))  # 1 day
    def get(self, request, *args, **kwargs):
        return super(TermsView, self).get(request, *args, **kwargs)
