#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4


class ShowcaseItem(object):

    def __init__(self, img_src, alt=None, title=None, url=None, target=None):
        self._img_src = img_src
        self._alt = alt
        self._title = title
        self._url = url
        self._target = target

    @property
    def img_src(self):
        return self._img_src

    @img_src.setter
    def img_src(self, value):
        self._img_src = value

    @property
    def alt(self):
        return self._alt

    @alt.setter
    def alt(self, value):
        self._alt = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, value):
        self._target = value
