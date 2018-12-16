#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.utils.translation import ugettext_lazy as _

from .base import *  # NOQA

USE_I18N = True

LANGUAGES = (
    ('en-us', _('English')),
    ('fa', _('Farsi')),
)

TEMPLATES[0]['OPTIONS'] = {
    'debug': DEBUG,
    'context_processors': (
        'django.template.context_processors.i18n',
        'django.template.context_processors.static',
    ),
    # List of callables that know how to import templates from
    # various sources.
    'loaders': (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )
}

INSTALLED_APPS += (
)
