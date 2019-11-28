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
        self.db = pymysql.connect("localhost", "root", "123456", "house", charset="utf8")
        self.cursor = self.db.cursor()

        # 从数据库读取区域，按照区域查询数据
        results = self.get_areas()
        urls = []
        for area_item in results:
            urls.append('https://chongqing.anjuke.com/sale/' + area_item[1] + '/')
            # break

        self.start_urls = urls
        self.enable_next_page = True

    def close(self):
        self.db.close()

    def get_areas(self):
        # 区域数量太多，会触发人机校验，请求连接会跳转到人工操作页面，这里添加条件只获取部分区域
        select_sql = "select * from house_area where parent_id > 0"
        # select_sql = "select * from house_area where id = 1"

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
            house_item['title'] = item.css('.house-title a::text').extract_first().strip()
            house_item['url'] = item.css('.house-title a::attr(href)').extract_first().strip()
            # 总价万为单位
            house_item['total_price'] = re.search('\d+', item.css('.pro-price .price-det').extract_first().strip()).group()
            house_item['code'] = ''
            if house_item['url']:
                search_code = re.search(pat_code, house_item['url'])
                if search_code:
                    house_item['code'] = search_code.group(1)
            house_item['community'] = ''
            house_item['location'] = item.css('.details-item:nth-child(3) span.comm-address::attr(title)').extract_first().replace(u'\xa0', u' ').strip()
            if house_item['location']:
                address_items = re.split('\s+', house_item['location'])
                if len(address_items) > 1:
                    house_item['community'] = address_items[0]

            house_item['build_years'] = item.css('.details-item:nth-child(2) span:nth-child(7)::text').extract_first().strip()
            house_item['floor'] = item.css('.details-item:nth-child(2) span:nth-child(5)::text').extract_first().strip()
            house_item['layout'] = item.css('.details-item:nth-child(2) span:nth-child(1)::text').extract_first().strip()
            house_item['size'] = item.css('.details-item:nth-child(2) span:nth-child(3)::text').extract_first().strip()
            house_item['picture_url'] = item.css('.item-img img::attr(src)').extract_first().strip()

            house_item['unit_price'] = re.search('\d+', item.css('.pro-price .unit-price::text').extract_first().strip()).group()

            yield house_item
        
        #分页操作
        next_page = response.css('.multi-page a.aNxt::attr(href)').extract_first()
        if self.enable_next_page and next_page:
            #构建新的Request对象
            next_url = next_page.strip()
            yield scrapy.Request(next_url, callback=self.parse)