#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.urls import path
from .views import VideosView

app_name = 'videos'

urlpatterns = [
    path('introduction/', VideosView.as_view(), name='index'),
    path('introduction/<amp:amp>/', VideosView.as_view(), name='index-amp'),
]
