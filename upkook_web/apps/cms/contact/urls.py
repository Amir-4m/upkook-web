#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.urls import path
from .views import ContactView

app_name = 'contact'

urlpatterns = [
    path('contact-us/', ContactView.as_view(), name='index'),
    path('contact-us/<amp:amp>/', ContactView.as_view(), name='index-amp'),
]
