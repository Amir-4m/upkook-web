#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from datetime import datetime

from django.conf import settings
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control, cache_page
from django.utils.translation import gettext_lazy as _

from upkook_web.apps.cms.videos.services import VideosService

from django_contrib.video_content.aparat import AparatVideo


intro_video = AparatVideo(
    identity=settings.INTRO_APARAT_VIDEO_ID,
    title=_("Videos Intro Video Title"),
    description=_("Videos Intro Video Description"),
    src=settings.INTRO_APARAT_VIDEO_SRC,
    amp_src=settings.INTRO_APARAT_VIDEO_AMP_SRC
)


@method_decorator(cache_control(max_age=1 * 24 * 60 * 60), name='get')  # 1 day
@method_decorator(cache_page(1 * 24 * 60 * 60), name='get')  # 1 day
class VideosView(TemplateView):
    http_method_names = ['get']
    template_name = 'videos/videos.html'
    last_modification = datetime(2019, 11, 25)

    def get_context_data(self, amp=None):
        context = super(VideosView, self).get_context_data(amp=amp)
        context.update({
            'title': _('Videos | Intro Video Title'),
            'description': _('Videos Intro Video Page Description')
        })

        if amp == 'amp' or self.request.GET:
            context.update({'canonical_url': VideosService.get_index_absolute_url(self.request, is_amp=False)})
        if amp != 'amp':
            context.update({'amp_url': VideosService.get_index_absolute_url(self.request, is_amp=True)})
        context.update({
            "intro_video": intro_video
        })
        return context
