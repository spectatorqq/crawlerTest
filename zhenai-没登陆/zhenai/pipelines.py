# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb

conn = MySQLdb.connect(host='localhost', port=3306, user='root', password='123456',
                       db='crawler', charset='utf8')
cursor = conn.cursor()


class ZhenaiPipeline(object):
    def process_item(self, item, spider):
        items = item['fake_love']
        # print(items)
        sql = 'insert into fake_love values(%s, %s, %s, %s)'
        cursor.executemany(sql, items)
        conn.commit()
        return item
