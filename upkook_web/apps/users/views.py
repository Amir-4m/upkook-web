#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.conf import settings
from django.urls import reverse
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from datetime import datetime
from django.views.decorators.cache import cache_control, cache_page
from django.utils.translation import ugettext_lazy as _
from django_contrib.html.link import Link
from django_contrib.sites.services import SiteService


@method_decorator(cache_control(max_age=1 * 24 * 60 * 60), name='get')  # 1 day
@method_decorator(cache_page(1 * 24 * 60 * 60), name='get')  # 1 day
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
                'user_track_id_key': settings.AUTH_USER_TRACK_ID_COOKIE_NAME,
            }
        })
        return context


class SignInView(UserViewBase):
    template_name = 'users/sign-in.html'
    view_name = 'users:sign-in'
    last_modification = datetime(2019, 8, 26)

    def get_context_data(self):
        context = super(SignInView, self).get_context_data()
        context.update({
            'sign_up_url': reverse(SignUpView.view_name),
            'forgot_password_url': reverse(ForgotPassword.view_name),
            'title': _('Welcome, log in to UPKOOK - UPKOOK'),
            'description': _('Log in to UPKOOK customer experience measurement platform control panel')
        })
        return context


class SignUpView(UserViewBase):
    template_name = 'users/sign-up.html'
    view_name = 'users:sign-up'
    last_modification = datetime(2019, 8, 26)

    def get_context_data(self):
        context = super(SignUpView, self).get_context_data()
        context.update({
            'title': _('Free registration in UPKOOK - UPKOOK'),
            'description': _(
                'Free registration in UPKOOK customer experience measurement platform, '
                'create survey, share survey link, customer satisfaction measurement and result analysis'
            )

        })
        return context


class ForgotPassword(UserViewBase):
    template_name = 'users/forgot-password.html'
    view_name = 'users:forgot-password'
    last_modification = datetime(2019, 8, 26)

    def get_context_data(self):
        context = super(ForgotPassword, self).get_context_data()
        context.update({
            'sign_up_url': reverse(SignUpView.view_name),
            'sign_in_url': reverse(SignInView.view_name),
            'title': _('Forgot Password - UPKOOK')

        })
        return context
