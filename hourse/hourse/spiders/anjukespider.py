import scrapy
import re
from hourse.items import AnjukeCQItem


class AnjukeSpider(scrapy.Spider):
    name = 'anjuke'

    allow_domains = ["anjuke.com"]

    start_urls = [
        'https://chongqing.anjuke.com/sale/p1/',
    ]

    def parse(self, response):
        # house_list = response.xpath('//li[@class="list-item"]')
        house_list = response.css('li.list-item')

        house_item = AnjukeCQItem()
        pat_code = '/([a-zA-Z0-9]+)\?'

        for item in house_list:
            # house_item['house_title'] = item.xpath('/div[@class="house-details"]/div[@class="house-title"]/a[0]/text()').extract().strip()
            # house_item['house_url'] = item.xpath('/div[@class="house-details"]/div[@class="house-title"]/a[0]/@href').extract().strip()
            house_item['house_title'] = item.css('.house-title a::text').extract_first().strip()
            house_item['house_url'] = item.css('.house-title a::attr(href)').extract_first().strip()
            house_item['house_cost'] = re.search('\d+', item.css('.pro-price .price-det').extract_first().strip()).group()
            house_item['house_code'] = ''
            if house_item['house_url']:
                search_code = re.search(pat_code, house_item['house_url'])
                if search_code:
                    house_item['house_code'] = search_code.group(1)
            house_item['house_public_time'] = ''
            house_item['house_community'] = ''
            house_item['house_location'] = item.css('.details-item:nth-child(3) span.comm-address::attr(title)').extract_first().replace(u'\xa0', u' ').strip()
            if house_item['house_location']:
                address_items = re.split('\s+', house_item['house_location'])
                if len(address_items) > 1:
                    house_item['house_community'] = address_items[0]

            house_item['house_build_years'] = item.css('.details-item:nth-child(2) span:nth-child(7)::text').extract_first().strip()
            house_item['house_kind'] = item.css('.details-item:nth-child(2) span:nth-child(5)::text').extract_first().strip()
            house_item['house_layout'] = item.css('.details-item:nth-child(2) span:nth-child(1)::text').extract_first().strip()
            house_item['house_size'] = item.css('.details-item:nth-child(2) span:nth-child(3)::text').extract_first().strip()
            house_item['house_face_to'] = item.css('.item-img img::attr(src)').extract_first().strip()
            house_item['house_point'] = ''

            house_item['house_price'] = re.search('\d+', item.css('.pro-price .unit-price::text').extract_first().strip()).group()
            house_item['house_first_pay'] = ''
            house_item['house_month_pay'] = ''
            house_item['house_decorate_type'] = ''
            house_item['house_agent'] = ''
            house_item['house_agency'] = ''

            yield house_item
        
        #分页操作
        next_url = response.css('.multi-page a.aNxt::attr(href)').extract_first().strip()
        if next_url and not next_url.strip():
            #构建新的Request对象
            yield scrapy.Request(next_url, callback=self.parse)