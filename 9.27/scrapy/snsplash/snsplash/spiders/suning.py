# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider, Request
from urllib.parse import quote
from snsplash.items import SnsplashItem
from scrapy_splash import SplashRequest

#%d匹配后面的args.page,返回执行js后的页面
script2 = """
function main(splash,args)
  splash.images_enabled = false
  assert(splash:go(args.url))
  assert(splash:wait(args.wait))
  js = string.format("document.querySelector('#bottomPage').value=%d;
       document.querySelector('.ensure').click();",args.page)
  splash:evaljs(js)
  assert(splash:wait(args.wait))
  return splash:html()
end
"""
script = """
function main(splash,args)
  splash.images_enabled = false
  assert(splash:go(args.url))
  assert(splash:wait(args.wait))
  return splash:html()
end
"""
script3 = """
function main(splash,args)
  splash.images_enabled = false
  assert(splash:go(args.url))
  assert(splash:wait(3))
  js = "document.querySelector('#bottomPage').value='3';document.querySelector('.page-more.ensure').click()"
  splash:evaljs(js)
  assert(splash:wait(3))
  return splash:html()
end
"""
class SuningSpider(scrapy.Spider):
    name = 'suning'
    allowed_domains = ['www.suning.com']
    #base_urls = ['https://search.suning.com/']

    def start_requests(self):
        for keyword in self.settings.get('KEYWORDS'):
            #for page in range(1,self.settings.get('MAX_PAGE') + 1):
            for page in range(1,10):
                #url = self.base_urls + quote(keyword)
                url = 'https://search.suning.com/iPhone/'
                yield SplashRequest(url,callback=self.parse,endpoint='execute',
                                    args={'lua_source':script,'page':page,'wait':3})

    def parse(self, response):
        list = response.xpath('//ul[@class="clearfix"]/li')
        if list:
            for onegoods in list:
                item = SnsplashItem()
                item['title'] = ''.join(onegoods.xpath('.//img[@class="search-loading"]/@alt').extract()).strip()
                item['comment'] = ''.join(onegoods.xpath('.//a[@class="num"]/text()').extract()).strip()
                item['shop'] = ''.join(onegoods.xpath('.//a[@sa-data="{eletp:shop}"]/text()').extract()).strip()
                yield item
        













    
