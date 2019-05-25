#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.conf import settings
from django.urls import reverse
from django.views.generic import TemplateView
from django.utils.translation import ugettext_lazy as _
from django_contrib.html.link import Link
from django_contrib.sites.services import SiteService


class UserViewBase(TemplateView):
    http_method_names = ['get']

    def get_context_data(self):
        context = super(UserViewBase, self).get_context_data()
        site = SiteService.get_current_site(self.request)
        context.update({'title': site.name})

        context.update({'footer_links': [
            Link(href='https://www.upkook.com/', text=_('UPKOOK'), target='_blank'),
            Link(href='https://blog.upkook.com/', text=_('Blog'), target='_blank'),
            Link(href='https://policies.upkook.com/terms/', text=_('Terms of Service'), target='_blank'),
            Link(href='https://policies.upkook.com/privacy/', text=_('Privacy Policy'), target='_blank')
        ]})

        context.update({
            'dashboard_url': settings.DASHBOARD_URL,
            'auth_cookie': {
                'age': settings.AUTH_COOKIE_AGE,
                'domain': settings.AUTH_COOKIE_DOMAIN,
                'path': settings.AUTH_COOKIE_PATH,
                'secure': settings.AUTH_COOKIE_SECURE,
                'access_key': settings.AUTH_ACCESS_COOKIE_NAME,
                'refresh_key': settings.AUTH_REFRESH_COOKIE_NAME,
            }
        })
        return context


class SignInView(UserViewBase):
    template_name = 'users/sign-in.html'
    view_name = 'users:sign-in'

    def get_context_data(self):
        context = super(SignInView, self).get_context_data()
        context.update({'sign_up_url': reverse(SignUpView.view_name)})
        return context


class SignUpView(UserViewBase):
    template_name = 'users/sign-up.html'
    view_name = 'users:sign-up'

    def get_context_data(self):
        context = super(SignUpView, self).get_context_data()
        context.update({'sign_in_url': reverse(SignInView.view_name)})
        return context
