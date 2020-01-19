#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.urls import path
from .views import TermsView, IndexView, PrivacyView

app_name = 'policies'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<amp:amp>/', IndexView.as_view(), name='index-amp'),
    path('terms/', TermsView.as_view(), name='terms'),
    path('terms/<amp:amp>/', TermsView.as_view(), name='terms-amp'),
    path('privacy/', PrivacyView.as_view(), name='privacy'),
    path('privacy/<amp:amp>/', PrivacyView.as_view(), name='privacy-amp'),
]
