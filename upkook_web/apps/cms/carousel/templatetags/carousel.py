#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.template import Library
register = Library()


@register.inclusion_tag('carousel/carousel-base.html')
def carousel(title, items, is_amp=False):
    return {
        "title": title,
        "items": items,
        "is_amp": is_amp
    }
