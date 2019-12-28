#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from datetime import datetime
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView

from .services import FeaturesService

features_col_1 = [
    _("features all-features col1 item1"),
    _("features all-features col1 item2"),
    _("features all-features col1 item3"),
    _("features all-features col1 item4"),
    _("features all-features col1 item5"),
    _("features all-features col1 item6"),
    _("features all-features col1 item7"),
    _("features all-features col1 item8"),
    _("features all-features col1 item9"),
]

features_col_2 = [
    _("features all-features col2 item1"),
    _("features all-features col2 item2"),
    _("features all-features col2 item3"),
    _("features all-features col2 item4"),
    _("features all-features col2 item5"),
    _("features all-features col2 item6"),
]


class FeaturesView(TemplateView):
    http_method_names = ['get']
    template_name = 'features/features.html'
    last_modification = datetime(2019, 12, 28)

    def get_context_data(self, amp=None):
        context = super(FeaturesView, self).get_context_data(amp=amp)
        context.update({
            'title': _('Features | Upkook Startup'),
            'description': _("Features Page Description")
        })
        if amp == 'amp' or self.request.GET:
            context.update({'canonical_url': FeaturesService.get_index_absolute_url(self.request, is_amp=False)})
        if amp != 'amp':
            context.update({'amp_url': FeaturesService.get_index_absolute_url(self.request, is_amp=True)})

        context.update({
            "features_col_1": features_col_1,
            "features_col_2": features_col_2
        })

        return context
