# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IndexItem(scrapy.Item):
    index = scrapy.Field()
    country = scrapy.Field()
    last = scrapy.Field()
    high = scrapy.Field()
    low = scrapy.Field()
    changeTotal = scrapy.Field()
