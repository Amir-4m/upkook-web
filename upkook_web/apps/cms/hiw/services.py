#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.urls import reverse


class HIWService(object):
    @staticmethod
    def get_index_relative_url(is_amp=False):
        if is_amp:
            return reverse('hiw:hiw-amp', kwargs={'amp': 'amp'})
        return reverse('hiw:hiw')

    @staticmethod
    def get_index_absolute_url(request, is_amp=False):
        return '{scheme}://{host}{path}'.format(
            scheme=request.scheme, host=request.get_host(),
            path=HIWService.get_index_relative_url(is_amp)
        )
