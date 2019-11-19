#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django import template

register = template.Library()


@register.inclusion_tag('home/includes/quote.html', name='quote')
def quote(quote, title, is_amp=False):
    return {
        "quote": quote,
        "title": title,
        "is_amp": is_amp
    }


@register.inclusion_tag('home/includes/product_intro_box.html', name='product_intro_box')
def product_intro_box(desc, image=None, is_amp=False, alt=None, link=None):
    return {
        "image": image,
        "alt": alt,
        "desc": desc,
        "link": link,
        "is_amp": is_amp
    }


@register.inclusion_tag('home/includes/product_intro_list.html', name='product_intro_list')
def product_intro_list(title, items, is_amp=False):
    return {
        "title": title,
        "items": items,
        "is_amp": is_amp
    }


@register.inclusion_tag('home/includes/product_primary_description.html', name='product_primary_description')
def product_primary_description(description):
    return {
        "description": description,
    }


@register.inclusion_tag('home/includes/product.html', name='product')
def product_section(product, is_grey_bg=False, is_amp=False):
    return {
        "product": product,
        "is_grey_bg": is_grey_bg,
        "is_amp": is_amp
    }
