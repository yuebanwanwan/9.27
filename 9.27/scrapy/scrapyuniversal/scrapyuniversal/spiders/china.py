# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapyuniversal.items import NewsItem
from scrapyuniversal.ItemLoader import ChinaLoader


class ChinaSpider(CrawlSpider):
    name = 'china'
    allowed_domains = ['china.com']
    start_urls = ['https://travel.china.com/hotspot/']

    #定义爬取网站的规则
    rules = (
        #获取具有所需数据的页面(提取页面)
        Rule(LinkExtractor(allow='https://travel.china.com.*?html',
                           restrict_xpaths='//div[@class="r2_l"]//div[@class="m_L"]'), callback='parse_item'),
        #该Rule提取的链接需要跟进(跟进页面,表示该页面包含的链接会继续被rules筛选)
        #总结：不需要继续跟进的链接的解析函数一般为自定义的parse_item,而需要跟进的链接的解析函数一般为定义的多个Rule(),:D
        Rule(LinkExtractor(restrict_xpaths='//div[@class="pages"]//a[@class="nextPage"]/@href'))
    )

    def parse_item2(self, response):
        item = NewsItem()
        item['title'] = response.xpath('//title/text()').extract_first().strip()
        item['url'] = response.url
        item['text'] = ''.join(response.xpath('//div[@id="chan_newsDetail"]//p/text()').extract()).strip()
        item['datetime'] = response.xpath('//div[@id="chan_newsInfo"]/text()').re_first('(\d+-\d+-\d+\s\d+:\d+:\d+)')
        item['source'] = response.xpath('//div[@id="chan_newsInfo"]/text()').re_first('(;.*?;)')
        item['website'] = '中华网'
        yield item

    def parse_item(self, response):
        loader = ChinaLoader(item=NewsItem(),response=response)
        loader.add_xpath('title','//title/text()')
        loader.add_value('url',response.url)
        loader.add_xpath('text','//div[@id="chan_newsDetail"]//p/text()')
        loader.add_xpath('datetime','//div[@id="chan_newsInfo"]/text()',re='(\d+-\d+-\d+\s\d+:\d+:\d+)')
        loader.add_xpath('source','//div[@id="chan_newsInfo"]/text()')
        loader.add_value('website','中华网')
        yield  loader.load_item()












