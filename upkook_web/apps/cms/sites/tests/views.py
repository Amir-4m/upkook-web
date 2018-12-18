#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.shortcuts import render


def request_site(request):
    return render(request, 'test_context_processor/request_site.html')
