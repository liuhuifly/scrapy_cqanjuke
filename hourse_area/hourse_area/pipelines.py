# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class HourseAreaPipeline(object):
    def __init__(self):
        self.db = pymysql.connect("localhost", "root", "123456", "house", charset="utf8")
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()

    def process_item(self, item, spider):
        select_sql = "select id from house_area where code='%s'" % item['code']
        already_save = self.cursor.execute(select_sql)
        self.db.commit()

        if already_save == 1:
            # 更新
            update_sql = "update house_area set name='%s' where code='%s'" % (item['name'], item['code'])
            self.cursor.execute(update_sql)
            self.db.commit()
        else:
            parent_id = 0

            # 查询父级区域
            if item['parent_code']:
                select_sql = "select id from house_area where code='%s'" % item['parent_code']
                already_save = self.cursor.execute(select_sql)
                house_area = self.cursor.fetchone()
                self.db.commit()

                if already_save == 1:
                    parent_id = house_area[0]

            # 插入
            insert_sql = "insert into house_area(code,name,parent_id,parent_code,display_order)\
                values('%s','%s','%d','%s','%d')"\
                %(item['code'],item['name'],parent_id,item['parent_code'],item['display_order'])
            self.cursor.execute(insert_sql)
            self.db.commit()
        return item
