# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

conn = pymongo.MongoClient('mongodb://localhost')
db = conn['mymongo']
col = db['house']


class HousePipeline(object):
    def process_item(self, item, spider):
        city = item['city']
        region = item['region']
        adv = item['adv']
        discount = item['discount']
        col.insert({'city': city, 'region': region, 'adv': adv, 'discount': discount})
        return item
