# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class HoursePipeline(object):
    def __init__(self):
        self.db = pymysql.connect("localhost", "root", "123456", "house", charset="utf8")
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        select_area_sql = "select id from house_area where code='%s'" % item['area_code']
        is_area_exist = self.cursor.execute(select_area_sql)
        house_area = self.cursor.fetchone()
        area_id = 0
        if house_area:
            area_id = house_area[0]

        select_sql = "select id from house where code='%s'" % item['code']
        already_save = self.cursor.execute(select_sql)
        house_item = self.cursor.fetchone()
        self.db.commit()

        if already_save == 1:
            # 更新信息
            house_id = house_item[0]
            update_sql = "update house set title='%s', unit_price='%d', total_price='%d', url='%s' where id='%d'" % (item['title'],int(item['unit_price']),int(item['total_price']),item['url'],int(house_id))
            self.cursor.execute(update_sql)
            self.db.commit()

            # 插入价格
            self.add_price(house_id, item['code'], item['unit_price'], item['total_price'])  
        else:
            # 插入信息
            sql = "insert into house(area_id,area_code,title,unit_price,total_price,code,community,location,build_years,floor,layout,size,picture_url,url)\
                values('%d','%s','%s','%d','%d','%s','%s','%s','%s','%s','%s','%s','%s','%s')"\
                %(area_id,item['area_code'],item['title'],int(item['unit_price']),int(item['total_price']),item['code'],item['community'],item['location'],\
                    item['build_years'],item['floor'], item['layout'],item['size'],item['picture_url'],item['url'])
            self.cursor.execute(sql)

            house_id = int(self.db.insert_id())
            self.db.commit()

            # 插入价格
            self.add_price(house_id, item['code'], item['unit_price'], item['total_price'])  
        return item

    def add_price(self, house_id, house_code, unit_price, total_price):
        sql = "insert into house_price(house_id, house_code, unit_price, total_price)\
            values('%d','%s','%d','%d')" % (int(house_id), house_code, int(unit_price), int(total_price))
        self.cursor.execute(sql)
        self.db.commit() 

    def __del__(self):
        self.db.close()
