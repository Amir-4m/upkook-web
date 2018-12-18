#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

urlpatterns = [
    url(
        r'^robots\.txt$',
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
        name='robots'
    ),
]

# This is only needed when using runserver.
if settings.DEBUG:  # pragma: no cover
    dev_urlpatterns = static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT,
    )
    dev_urlpatterns += staticfiles_urlpatterns()
    urlpatterns = dev_urlpatterns + urlpatterns
