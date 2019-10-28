#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.urls import path
from .views import SignInView, SignUpView, ForgotPassword

app_name = 'users'

urlpatterns = [
    path('login/', SignInView.as_view(), name='sign-in'),
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('users/password/forgot/', ForgotPassword.as_view(), name='forgot-password'),
]
