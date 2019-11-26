# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HourseItem(scrapy.Item):
    area_code = scrapy.Field()
    house_title = scrapy.Field()
    house_cost = scrapy.Field()
    house_code = scrapy.Field()
    house_community = scrapy.Field()
    house_location = scrapy.Field()
    house_build_years = scrapy.Field()
    house_kind = scrapy.Field()
    house_layout = scrapy.Field()
    house_size = scrapy.Field()
    house_face_to = scrapy.Field()
    house_price = scrapy.Field()
    house_url = scrapy.Field()

class AnjukeItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    image = scrapy.Field()
    shi = scrapy.Field()
    ting = scrapy.Field()
    area = scrapy.Field()
    floor = scrapy.Field()
    unit_price = scrapy.Field()
    total_price = scrapy.Field()
    create_year = scrapy.Field()
    village = scrapy.Field()
    province = scrapy.Field()
    city = scrapy.Field()
    region = scrapy.Field()
    address = scrapy.Field()
    create_time = scrapy.Field()
    update_time = scrapy.Field()

class AnjukeCQArea(scrapy.Item):
    code = scrapy.Field()
    name = scrapy.Field()
    parent_code = scrapy.Field()
    display_order = scrapy.Field()

class AnjukeCQItem(scrapy.Item):
    house_title = scrapy.Field()
    house_cost = scrapy.Field()
    house_code = scrapy.Field()
    house_public_time = scrapy.Field()
    house_community = scrapy.Field()
    house_location = scrapy.Field()
    house_build_years = scrapy.Field()
    house_kind = scrapy.Field()
    house_layout = scrapy.Field()
    house_size = scrapy.Field()
    house_face_to = scrapy.Field()
    house_point = scrapy.Field()
    house_price = scrapy.Field()
    house_first_pay = scrapy.Field()
    house_month_pay = scrapy.Field()
    house_decorate_type = scrapy.Field()
    house_agent = scrapy.Field()
    house_agency = scrapy.Field()
    house_url = scrapy.Field()