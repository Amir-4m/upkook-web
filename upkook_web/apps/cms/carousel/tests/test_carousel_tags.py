#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.test import TestCase
from django.template import Context, Template
from upkook_web.apps.cms.home.views import CarouselItem


class CarouselTestCase(TestCase):
    def test_carousel_with_url(self):
        carousel_item = CarouselItem(
            img_src='/static/home/images/huawei.png',
            description='test',
            alt='first pic',
            url='https://npsbenchmarks.com/companies/huawei',
            target='_blank'
        )
        context = Context({
            'title': 'test title',
            'items': [carousel_item]
        })
        template = Template('{% load carousel %}{% carousel title items %}')

        html = template.render(context)

        expected_html = (
            """
           <div class="car-wrapper">
            <h2>test title</h2>
            <div class="md-gr">
            <div class="md-cl--3-col md-cl--4-col-phone md-cl--8-col-tablet options">
            <ul>
            <li class="slide-caption" data-slide="product-slide-1" id="product-slide-1-caption">
            <h3>test</h3>
            </li>
           <li class="demo">
          <a class="lg-demo" href="https://demo.upkook.com"
             target="_blank">Try Demo &larr;</a>

        </li>
      </ul>
    </div>
    <br>
    <div class="md-cl--9-col md-cl--8-col-tablet md-cl--4-col-phone">
      <div class="md-slideshow-container">
        <!-- Full-width images with number and caption text -->
        <div class="car-slide fade" id="product-slide-1">
        <h3 class="sm-description">test</h3>
          <a href="https://npsbenchmarks.com/companies/huawei"  target="_blank">
          <img class="slide-medium" src="/static/home/images/huawei.png" alt="first pic" >
          </a>
        </div>
        <div class="slideshow-dots md-cl--4-col-phone">
          <span class="slide-dot" data-slide="product-slide-1" id="product-slide-1-dot"></span>
          </div>
          <a class="mdl-button mdl-button--accent mdl-js-button sm-demo" href="https://demo.upkook.com" target="_blank">
            Try Demo &larr;
          </a>
      </div>
    </div>
  </div>
</div>
    """

        )

        self.assertHTMLEqual(html, expected_html)

    def test_carousel_without_url(self):
        carousel_item = CarouselItem(
            img_src='/static/home/images/huawei.png',
            description='test',
            alt='first pic',
        )
        context = Context({
            'title': 'test title',
            'items': [carousel_item]
        })
        template = Template('{% load carousel %}{% carousel title items %}')

        html = template.render(context)

        expected_html = (
            """
                        <div class="car-wrapper">
                        <h2>test title</h2>
                        <div class="md-gr">
                        <div class="options md-cl--3-col md-cl--8-col-tablet md-cl--4-col-phone">
                        <ul>
                        <li class="slide-caption" data-slide="product-slide-1" id="product-slide-1-caption">
                        <h3>
                        test
                        </h3>
                        </li>
                       <li class="demo">
                      <a class="lg-demo" href="https://demo.upkook.com"
             target="_blank">Try Demo &larr;</a>

                    </li>
                  </ul>
                </div>
                <br>
                <div class="md-cl--9-col md-cl--8-col-tablet md-cl--4-col-phone">
                  <div class="md-slideshow-container">
                    <!-- Full-width images with number and caption text -->
                    <div class="car-slide fade" id="product-slide-1">
                      <h3 class="sm-description">test</h3>
                      <img class="slide-medium" src="/static/home/images/huawei.png" alt="first pic" >
                    </div>
                    <div class="slideshow-dots md-cl--4-col-phone">
                   <span class="slide-dot" data-slide="product-slide-1" id="product-slide-1-dot"></span>
                   </div>
                   <a class="mdl-button mdl-button--accent mdl-js-button sm-demo" href="https://demo.upkook.com" target="_blank">
                     Try Demo &larr;
                   </a>
                  </div>
                </div>
              </div>
            </div>
                """

        )
        self.assertHTMLEqual(html, expected_html)

    def test_carousel_small_image(self):
        carousel_item = CarouselItem(
            img_src='/static/home/images/huawei.png',
            img_src2='/static/home/images/huawei.png',
            description='test',
            alt='first pic',
        )
        context = Context({
            'title': 'test title',
            'items': [carousel_item]
        })
        template = Template('{% load carousel %}{% carousel title items %}')

        html = template.render(context)

        expected_html = (
            """
                        <div class="car-wrapper">
                        <h2>test title</h2>
                        <div class="md-gr">
                        <div class="options md-cl--3-col md-cl--8-col-tablet md-cl--4-col-phone">
                        <ul>
                        <li class="slide-caption" data-slide="product-slide-1" id="product-slide-1-caption">
                        <h3>
                        test
                        </h3>
                        </li>
                       <li class="demo">
                      <a class="lg-demo" href="https://demo.upkook.com"
             target="_blank">Try Demo &larr;</a>

                    </li>
                  </ul>
                </div>
                <br>
                <div class="md-cl--9-col md-cl--8-col-tablet md-cl--4-col-phone">
                  <div class="md-slideshow-container">
                    <!-- Full-width images with number and caption text -->
                    <div class="car-slide fade" id="product-slide-1">
                     <h3 class="sm-description">test</h3>
                      <img class="slide-medium" src="/static/home/images/huawei.png" alt="first pic" >
                       <img class="slide-small" src="/static/home/images/huawei.png" alt="first pic"/>

                    </div>
                    <div class="slideshow-dots md-cl--4-col-phone">
          <span class="slide-dot" data-slide="product-slide-1" id="product-slide-1-dot"></span>
          </div>
          <a class="mdl-button mdl-button--accent mdl-js-button sm-demo" href="https://demo.upkook.com" target="_blank">
            Try Demo &larr;
          </a>
                  </div>
                </div>
              </div>
            </div>
                """

        )
        self.assertHTMLEqual(html, expected_html)
