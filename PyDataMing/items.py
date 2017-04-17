# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PydatamingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    content = scrapy.Field()
    publish_date = scrapy.Field()
    title = scrapy.Field()
    reply = scrapy.Field()
    post = scrapy.Field()

