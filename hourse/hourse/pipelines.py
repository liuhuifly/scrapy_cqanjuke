# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class HoursePipeline(object):
    def __init__(self):
        self.db = pymysql.connect("localhost", "root", "123456", "pymysqldb", charset="utf8")
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):

        select_sql = "select * from house where house_code='%s'" % item['house_code']
        already_save = self.cursor.execute(select_sql)
        self.db.commit()

        if already_save == 1:
            # 更新
            pass
        else:
            # 插入
            sql = "insert into house(area_code,house_title,house_cost,house_code,house_community,house_location,house_build_years,house_kind,house_layout,house_size,\
                house_face_to,house_price,house_url)\
                values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"\
                %(item['area_code'],item['house_title'],item['house_cost'],item['house_code'],item['house_community'],item['house_location'],\
                    item['house_build_years'],item['house_kind'], item['house_layout'],item['house_size'],item['house_face_to'],item['house_price'],\
                    item['house_url'])
            self.cursor.execute(sql)
            self.db.commit()
        return item

    def __del__(self):
        self.db.close()

class AnjukePipeline(object):
    def __init__(self):
        self.db = pymysql.connect("localhost", "root", "123456", "pymysqldb", charset="utf8")
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):

        select_sql = "select * from cq_house_info where house_code='%s'" % item['house_code']
        already_save = self.cursor.execute(select_sql)
        self.db.commit()

        if already_save == 1:
            # 更新
            pass
        else:
            # 插入
            sql = "insert into cq_house_info(house_title,house_cost,house_code,house_public_time,house_community,house_location,house_build_years,house_kind,house_layout,house_size,\
                house_face_to,house_point,house_price,house_first_pay,house_month_pay,house_decorate_type,house_agent,house_agency,house_url)\
                values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"\
                %(item['house_title'],item['house_cost'],item['house_code'],item['house_public_time'],item['house_community'],item['house_location'],\
                    item['house_build_years'],item['house_kind'], item['house_layout'],item['house_size'],item['house_face_to'],item['house_point'],item['house_price'],\
                    item['house_first_pay'],item['house_month_pay'],item['house_decorate_type'],item['house_agent'],item['house_agency'],item['house_url'])
            self.cursor.execute(sql)
            self.db.commit()
        return item

    def __del__(self):
        self.db.close()

class AreaPipeline(object):
    def __init__(self):
        self.db = pymysql.connect("localhost", "root", "123456", "pymysqldb", charset="utf8")
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):

        select_sql = "select * from cq_area_info where code='%s'" % item['code']
        already_save = self.cursor.execute(select_sql)
        self.db.commit()

        if already_save == 1:
            # 更新
            pass
        else:
            # 插入
            sql = "insert into cq_area_info(code,name,parent_code,display_order)\
                values('%s','%s','%s','%d')"\
                %(item['code'],item['name'],item['parent_code'],item['display_order'])
            self.cursor.execute(sql)
            self.db.commit()
        return item

    def __del__(self):
        self.db.close()