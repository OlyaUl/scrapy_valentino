# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ValentinoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ValentinoProduct(scrapy.Item):
    site_product_id = scrapy.Field()
    name = scrapy.Field()
    model = scrapy.Field()
    category = scrapy.Field()
    description = scrapy.Field()
    material = scrapy.Field()
    made_in = scrapy.Field()
    url = scrapy.Field()
    image = scrapy.Field()
    site = scrapy.Field()


class ValentinoPrice(scrapy.Item):
    site_product_id = scrapy.Field()
    params = scrapy.Field()
    stock = scrapy.Field()
    currency = scrapy.Field()

