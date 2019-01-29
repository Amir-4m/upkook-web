#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4


class HomeService(object):
    @staticmethod
    def get_index_relative_url(is_amp=False):
        return '/amp/' if is_amp else ''

    @staticmethod
    def get_index_absolute_url(request, is_amp=False):
        return '{scheme}://{host}{path}'.format(
            scheme=request.scheme, host=request.get_host(),
            path=HomeService.get_index_relative_url(is_amp)
        )
