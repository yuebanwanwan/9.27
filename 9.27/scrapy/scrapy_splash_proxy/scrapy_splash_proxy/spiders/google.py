# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest

class GoogleSpider(scrapy.Spider):
    name = 'google'
    allowed_domains = ['http://httpbin.org']
    start_urls = ['http://httpbin.org/get']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url,callback=self.parse)

    def parse(self, response):
        print(response.text)
