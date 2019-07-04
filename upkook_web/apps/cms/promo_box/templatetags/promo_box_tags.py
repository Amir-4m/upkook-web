#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django import template
register = template.Library()


@register.inclusion_tag('promo_box/box.html', name='promo_box')
def promo_box(title, desc, button):
    return {
        "title": title,
        "button": button,
        "desc": desc,
    }
