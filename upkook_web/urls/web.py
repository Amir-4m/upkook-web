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

from . import urlpatterns

sitemaps = {
    'home': HomeSitemap,
    'about': AboutSitemap,
    'contact': ContactSitemap,
    'hiw': HIWSitemap,
    'users': UsersSitemap
}

urlpatterns += [
    path(
        'sitemap.xml',
        cache_page(24 * 60 * 60)(sitemap),
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'
    ),

    path('', include('upkook_web.apps.cms.home.urls', 'home')),
    path('', include('django_contrib.sites.urls.web', 'sites')),
    path('', include('upkook_web.apps.users.urls', 'users')),
    path('', include('upkook_web.apps.cms.hiw.urls', 'hiw')),
    path('', include('upkook_web.apps.cms.about.urls', 'about')),
    path('', include('upkook_web.apps.cms.contact.urls', 'contact')),

]
