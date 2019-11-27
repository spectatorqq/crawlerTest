# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb

conn = MySQLdb.connect(host='localhost', port=3306, user='root', password='123456',
                       db='crawler', charset='utf8')
cursor = conn.cursor()


class Job51Pipeline(object):
    def process_item(self, item, spider):
        sql = 'insert into job51 values(%s, %s, %s, %s)'
        cursor.execute(sql, (item['job'], item['company'], item['work_place'], item['salary']))
        conn.commit()
        return item
