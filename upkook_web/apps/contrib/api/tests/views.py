#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.shortcuts import render


def site(request):
    return render(request, 'tests_api/site.html')
