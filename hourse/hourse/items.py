# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class HourseItem(scrapy.Item):
    area_code = scrapy.Field()
    title = scrapy.Field()
    unit_price = scrapy.Field()
    total_price = scrapy.Field()
    code = scrapy.Field()
    community = scrapy.Field()
    location = scrapy.Field()
    build_years = scrapy.Field()
    floor = scrapy.Field()
    layout = scrapy.Field()
    size = scrapy.Field()
    picture_url = scrapy.Field()
    url = scrapy.Field()