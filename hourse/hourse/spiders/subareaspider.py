import scrapy
import re
from hourse.items import AnjukeCQArea

class SubAreaSpider(scrapy.Spider):
    name = 'areas'

    allow_domains = ["anjuke.com"]

    start_urls = [
        'https://chongqing.anjuke.com/sale/',
    ]

    def parse(self, response):
        area_lists = response.css('div.div-border.items-list div.items:first-child .elems-l a')

        area_item = AnjukeCQArea()
        display_order = 1
        for item in area_lists:
            href = item.css('::attr(href)').extract_first().strip()
            # href_items = re.split('/', href)

            area_item['code'] = href.replace('https://chongqing.anjuke.com/sale/','').replace('/','')
            area_item['name'] = item.css('::text').extract_first().strip()
            area_item['parent_code'] = ''
            area_item['display_order'] = display_order

            display_order += 1

            yield area_item

            yield scrapy.Request(href, callback=self.parse_subarea, meta={'parent_code': area_item['code']})
    
    def parse_subarea(self, response):
        subarea_lists = response.css('div.div-border.items-list div.items:first-child .elems-l .sub-items a')
        area_item = AnjukeCQArea()
        display_order = 1
        for item in subarea_lists:
            href = item.css('::attr(href)').extract_first().strip()
            # href_items = re.split('/', href)

            area_item['code'] = href.replace('https://chongqing.anjuke.com/sale/','').replace('/','')
            area_item['name'] = item.css('::text').extract_first().strip()
            area_item['parent_code'] = response.meta['parent_code']
            area_item['display_order'] = display_order

            display_order += 1

            yield area_item
