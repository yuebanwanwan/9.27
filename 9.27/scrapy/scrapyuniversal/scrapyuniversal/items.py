# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item ,Field

class NewsItem(Item):
    title = Field()
    url = Field()
    text = Field()
    datetime = Field()
    source = Field()
    website = Field()

class DadaochaotianItem(Item):
    collection = table = 'DaDaoChaoTian'

    title = Field()
    url = Field()
    text = Field()


