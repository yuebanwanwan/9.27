# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from lianjia.items import LianjiaItem

class BjlianjiaSpider(scrapy.Spider):
    name = 'bjlianjia'
    allowed_domains = ['lianjia.com']
    base_urls = 'https://bj.lianjia.com/zufang/pg'

    def start_requests(self):
        MAX_PAGE = 100
        for i in range(1,MAX_PAGE + 1):
            url = self.base_urls + str(i) + '/'
            yield Request(url = url ,callback=self.parse)




    def parse(self, response):
        #在框架里此response.xpath()返回的是Selector组成的list,Selector可以继续调用xpath()等方法进行解析
        allItem = response.xpath('//ul[@id="house-lst"]//li')
        if allItem:
            for item in allItem:
                Item = LianjiaItem()
                Item['title'] = item.xpath('.//h2//text()').extract_first().strip()
                #Item['price'] = item.xpath('.//div[@class="price"]//text()').extract_first().strip()
                #获取节点内的所有文本,拼接起来
                Item['price'] = ''.join(item.xpath('.//div[@class="price"]//text()').extract()).strip()
                yield Item