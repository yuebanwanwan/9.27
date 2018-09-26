# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from urllib.parse import urlencode
import json

from image360.items import ImageItem


class ImagesSpider(Spider):
    name = 'images'
    allowed_domains = ['images.so.com']
    start_urls = ['http://images.so.com/']
    
    
    def start_requests(self):
        data = {'q': '陈钰琪'}
        base_url = 'https://image.so.com/j?'
        #爬取30次每次爬取30张(默认每页30张)
        for page in range(1, 30 + 1):
            data['sn'] = page * 30
            params = urlencode(data)
            url = base_url + params
            print(url)
            yield Request(url, self.parse)
    
    def parse(self, response):
        #此result是一个字典类型
        result = json.loads(response.text)
        for image in result.get('list'):
            item = ImageItem()
            item['id'] = image.get('id')
            item['url'] = image.get('img')
            item['title'] = image.get('title')
            item['thumb'] = image.get('_thumb')
            yield item



if __name__ == '__main__':
    IS = ImagesSpider()
    for request in IS.start_requests():
        #print(request)
        pass
