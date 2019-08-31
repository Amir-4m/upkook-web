#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control, cache_page
from django.utils.translation import ugettext_lazy as _


@method_decorator(cache_control(max_age=1 * 24 * 60 * 60), name='get')  # 1 day
@method_decorator(cache_page(1 * 24 * 60 * 60), name='get')  # 1 day
class TermsView(TemplateView):
    http_method_names = ['get']
    template_name = 'policies/terms.html'

    def get_context_data(self, **kwargs):
        kwargs.update(
            {
                'title': _('Terms of Service – Privacy &amp; Terms – Upkook'),
                'nav_template': "policies/includes/navigation.html"
            }
        )
        return super(TermsView, self).get_context_data(**kwargs)


class IndexView(TemplateView):
    http_method_names = ['get']
    template_name = 'policies/index.html'

    def get_context_data(self, **kwargs):
        kwargs.update(
            {
                'title': _('Privacy &amp; Terms – Upkook'),
                'nav_template': "policies/includes/navigation.html"
            }
        )
        return super(IndexView, self).get_context_data(**kwargs)


class PrivacyView(TemplateView):
    http_method_names = ['get']
    template_name = 'policies/privacy.html'

    def get_context_data(self, **kwargs):
        kwargs.update(
            {'title': _('Privacy Policy – Privacy &amp; Terms – Upkook'),
             'nav_template': "policies/includes/navigation.html"
             }
        )
        return super(PrivacyView, self).get_context_data(**kwargs)
