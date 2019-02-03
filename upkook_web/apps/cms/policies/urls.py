#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.urls import path
from .views import TermsView

app_name = 'policies'

urlpatterns = [
    path('terms/', TermsView.as_view(), name='terms'),
    path('terms/<amp:amp>/', TermsView.as_view(), name='terms-amp'),
]
