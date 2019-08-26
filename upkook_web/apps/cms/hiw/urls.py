#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.urls import path
from .views import HIWView

app_name = 'hiw'

urlpatterns = [
    path('how-it-works/', HIWView.as_view(), name='hiw'),
    path('how-it-works/<amp:amp>/', HIWView.as_view(), name='hiw-amp'),
]