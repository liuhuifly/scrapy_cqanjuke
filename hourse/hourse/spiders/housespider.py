import scrapy
import re
import pymysql
from hourse.items import HourseItem


class HouseSpider(scrapy.Spider):
    name = 'house'

    allow_domains = ["anjuke.com"]

    # start_urls = [
    #     'https://chongqing.anjuke.com/sale/p1/',
    # ]

    def __init__(self):
        self.db = pymysql.connect("localhost", "root", "123456", "pymysqldb", charset="utf8")
        self.cursor = self.db.cursor()

        results = self.get_areas()
        urls = []
        for area_item in results:
            urls.append('https://chongqing.anjuke.com/sale/' + area_item[1] + '/')
            # break
        
        # if len(start_urls) == 0:
        #     start_urls.append('https://chongqing.anjuke.com/sale/p1/')

        self.start_urls = urls

    def close(self):
        self.db.close()

    def get_areas(self):
        select_sql = "select * from cq_area_info where parent_id = 3"

        self.cursor.execute(select_sql)

        results = self.cursor.fetchall()

        return results

    def parse(self, response):
        house_list = response.css('li.list-item')

        house_item = HourseItem()
        house_item['area_code'] = ''
        current_url = re.search('sale/([^/]+)/', response.url)
        if current_url:
            house_item['area_code'] = current_url.group(1)

        pat_code = '/([a-zA-Z0-9]+)\?'
        
        for item in house_list:
            house_item['house_title'] = item.css('.house-title a::text').extract_first().strip()
            house_item['house_url'] = item.css('.house-title a::attr(href)').extract_first().strip()
            house_item['house_cost'] = re.search('\d+', item.css('.pro-price .price-det').extract_first().strip()).group()
            house_item['house_code'] = ''
            if house_item['house_url']:
                search_code = re.search(pat_code, house_item['house_url'])
                if search_code:
                    house_item['house_code'] = search_code.group(1)
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

            house_item['house_price'] = re.search('\d+', item.css('.pro-price .unit-price::text').extract_first().strip()).group()

            yield house_item
        
        #分页操作
        next_page = response.css('.multi-page a.aNxt::attr(href)').extract_first()
        if next_page:
            #构建新的Request对象
            next_url = next_page.strip()
            yield scrapy.Request(next_url, callback=self.parse)