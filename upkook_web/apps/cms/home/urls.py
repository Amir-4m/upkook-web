#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.urls import path
from .views import HomeView

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('<amp:amp>/', HomeView.as_view(), name='index-amp'),
]
