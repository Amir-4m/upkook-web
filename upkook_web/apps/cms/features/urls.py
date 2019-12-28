#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.urls import path
from .views import FeaturesView

app_name = 'features'

urlpatterns = [
    path('', FeaturesView.as_view(), name='index'),
    path('<amp:amp>/', FeaturesView.as_view(), name='index-amp'),
]
