#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.conf import settings
from django.urls import register_converter, path, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

from django.urls.converters import StringConverter


class AMPConverter(StringConverter):
    regex = 'amp'


register_converter(AMPConverter, 'amp')

urlpatterns = [
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name='robots'),
    path('amp/', include('django_contrib.amp.urls', namespace='amp')),
]

# This is only needed when using runserver.
if settings.DEBUG:  # pragma: no cover
    dev_urlpatterns = static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT,
    )
    dev_urlpatterns += staticfiles_urlpatterns()
    urlpatterns = dev_urlpatterns + urlpatterns
