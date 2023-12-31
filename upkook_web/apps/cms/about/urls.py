#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.urls import path
from .views import AboutView

app_name = 'about'

urlpatterns = [
    path('', AboutView.as_view(), name='index'),
    path('<amp:amp>/', AboutView.as_view(), name='index-amp'),
]
