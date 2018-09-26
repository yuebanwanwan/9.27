# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider, Request
from urllib.parse import quote
from jd.items import JdItem
from scrapy_splash import SplashRequest


script = """
function main(splash,args)
  splash.images_enabled = false
  assert(splash:go(args.url))
  assert(splash:wait(1))
  js = string.format("document.querySelector('.input-txt').value=%d;document.querySelector('.btn.btn-default').click()",args.page)
  splash:evaljs(js)
  assert(splash:wait(1))
  return splash:html()
end
"""


class JingdongSpider(scrapy.Spider):
    name = 'jingdong'
    allowed_domains = ['www.jd.com']
    base_urls = ['https://search.jd.com/Search?keyword=']


    def start_requests(self):
        for keyword in self.settings.get('KEYWORDS'):
            for page in range(1,self.settings.get('MAX_PAGE') + 1):
                #url = self.base_urls + quote(keyword)
                url = 'https://search.jd.com/search?keyword=feijibei'
                yield SplashRequest(url,callback=self.parse,endpoint='execute',
                                    args={'lua_source':script,'page':page,'wait':3})


    def parse(self, response):
        goodslist = response.xpath('//ul[@class="gl-warp.clearfix"]//li')
        if list:
            for onegoods in goodslist:
                item = JdItem()
                item['price'] = ''.join(onegoods.xpath('.//div[@class="p-price"]/strong/text()').extract()).strip()
                item['title'] = ''.join(onegoods.xpath('.//div[@class="p-name"]//em/text()').extract()).strip()
                item['comment'] = ''.join(onegoods.xpath('.//div[@class="p-commit"]/strong/text()').extract()).strip()
                item['boss'] = ''.join(onegoods.xpath('.//div[@class="p-shopnum"]/a/text()').extract()).strip()
                yield item




