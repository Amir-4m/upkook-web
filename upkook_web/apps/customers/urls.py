#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.urls import path
from .views import SignInView

app_name = 'customers'

urlpatterns = [
    path('login/', SignInView.as_view(), name='sign-in')
]
