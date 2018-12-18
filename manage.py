#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

import os
import sys

from upkook_web import DEFAULT_SETTINGS_MODULE

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", DEFAULT_SETTINGS_MODULE)
    from django.core.management import execute_from_command_line  # NOQA

    os.environ.setdefault('UPKOOK_WEB_TEST', '%s' % ('test' in sys.argv))
    execute_from_command_line(sys.argv)
