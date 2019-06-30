#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django import template

register = template.Library()


@register.inclusion_tag('showcase/case.html', name='showcase')
def showcase(title, desc, items, is_amp=False):
    return {
        "title": title,
        "items": items,
        "desc": desc,
        "is_amp": is_amp
    }
