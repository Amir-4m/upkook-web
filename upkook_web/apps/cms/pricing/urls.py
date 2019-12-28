#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.urls import path
from .views import PricingView

app_name = 'pricing'

urlpatterns = [
    path('', PricingView.as_view(), name='index'),
    path('<amp:amp>/', PricingView.as_view(), name='index-amp'),
]
