#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control, cache_page
from django.views.generic import TemplateView
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from .services import HIWService


@method_decorator(cache_control(max_age=1 * 24 * 60 * 60), name='get')  # 1 day
@method_decorator(cache_page(1 * 24 * 60 * 60), name='get')  # 1 day
class HIWView(TemplateView):
    http_method_names = ['get']
    template_name = 'hiw/how-it-works.html'

    def get_context_data(self, amp=None):
        context = super(HIWView, self).get_context_data(amp=amp)
        context.update({'title': _('How It Works')})

        if amp == 'amp' or self.request.GET:
            context.update({'canonical_url': HIWService.get_index_absolute_url(self.request, is_amp=False)})
        if amp != 'amp':
            context.update({'amp_url': HIWService.get_index_absolute_url(self.request, is_amp=True)})

        context.update({
            'dashboard_url': settings.DASHBOARD_URL,
            'auth_cookie': {
                'age': settings.AUTH_COOKIE_AGE,
                'domain': settings.AUTH_COOKIE_DOMAIN,
                'path': settings.AUTH_COOKIE_PATH,
                'secure': settings.AUTH_COOKIE_SECURE,
                'access_key': settings.AUTH_ACCESS_COOKIE_NAME,
                'refresh_key': settings.AUTH_REFRESH_COOKIE_NAME,
                'user_track_id_key': settings.AUTH_USER_TRACK_ID_COOKIE_NAME,
            }
        })

        return context
