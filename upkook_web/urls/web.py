#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.views.decorators.cache import cache_page

from upkook_web.apps.cms.home.sitemap import HomeSitemap
from upkook_web.apps.users.sitemap import UsersSitemap
from upkook_web.apps.cms.hiw.sitemap import HIWSitemap
from upkook_web.apps.cms.about.sitemap import AboutSitemap
from upkook_web.apps.cms.contact.sitemap import ContactSitemap
from upkook_web.apps.cms.pricing.sitemap import PricingSitemap
from upkook_web.apps.cms.videos.sitemap import VideosSitemap

from . import urlpatterns

sitemaps = {
    'home': HomeSitemap,
    'pricing': PricingSitemap,
    'about': AboutSitemap,
    'contact': ContactSitemap,
    'hiw': HIWSitemap,
    'users': UsersSitemap,
    'videos': VideosSitemap,

}

urlpatterns += [
    path(
        'sitemap.xml',
        cache_page(24 * 60 * 60)(sitemap),
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'
    ),
    path('videos/', include('upkook_web.apps.cms.videos.urls', 'videos')),
    path('how-it-works/', include('upkook_web.apps.cms.hiw.urls', 'hiw')),
    path('about-us/', include('upkook_web.apps.cms.about.urls', 'about')),
    path('contact-us/', include('upkook_web.apps.cms.contact.urls', 'contact')),
    path('pricing/', include('upkook_web.apps.cms.pricing.urls', 'pricing')),  #
    path('features/', include('upkook_web.apps.cms.features.urls', 'features')),
    path('', include('upkook_web.apps.cms.home.urls', 'home')),
    path('', include('django_contrib.sites.urls.web', 'sites')),
    path('', include('upkook_web.apps.users.urls', 'users')),

]
