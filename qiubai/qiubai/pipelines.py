# -*- coding: utf-8 -*-
# import MySQLdb
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# conn = MySQLdb.connect(host='localhost',port=3306,user='root',password='123456',db='spider_man',charset='utf8')
# cursor = conn.cursor()

class QiubaiPipeline(object):
    def process_item(self, item, spider):
        # sql = "insert into joker values(%s,%s)"
        #
        # cursor.execute(sql,(item['title'],item['cont']))
        # conn.commit()

        with open('joker.txt','a+',encoding='utf-8') as f:
            f.write(item['title']+'\n')
            f.write(item['cont']+'\n')

        return item
