# -*- coding: utf-8 -*-
import scrapy
from scrapyboss.items import ScrapybossItem
import json
from lxml import etree


class BossSpider(scrapy.Spider):
    name = 'boss'
    allowed_domains = ['www.zhipin.com']
    #start_urls = ['http://www.zhipin.com/']
    #指定城市为成都并且要求全是"不限"
    start_urls = ['http://www.zhipin.com//c101270100/h_101270100/?query=Java']

    def parse(self, response):
        list = response.xpath('//div[@class="job-list"]//div[@class="job-primary"]')
        if list:
            for onejob in list:
                item = ScrapybossItem()
                item['job'] = ''.join(onejob.xpath('.//img[@class="search-loading"]/@alt').extract()).strip()
                item['salary'] = onejob.xpath('.//span[@class="red"]/text()')[0]
                item['address'] = onejob.xpath('.//div[@class="info-primary"]/p/text()')[0]
                yield item
        next = selector.xpath('//div[@class="page"]//a[@class="next"]/@href')
        if next:
            url = response.urljoin(next[0])
            yield scrapy.Request(url = url,callback = self.parse)
                     






