# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

conn = pymongo.MongoClient('mongodb://localhost')
db = conn['mymongo']
col = db['stock']


class StockPipeline(object):
    def process_item(self, item, spider):
        col.insert({
            'code': item['code'],
            'name': item['name'],
            'last_price': item['last_price'],
            'deal_price': item['deal_price'],
            'pe_ratio': item['pe_ratio']
        })
        return item
