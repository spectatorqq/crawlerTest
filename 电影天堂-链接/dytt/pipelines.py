# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

conn = pymongo.MongoClient('mongodb://localhost')
db = conn['movie']
col = db['dytt']


class DyttPipeline(object):
    def process_item(self, item, spider):
        film_name = item['film_name']
        link = item['link']
        col.insert({'film_name': film_name, 'link': link})
        return item
