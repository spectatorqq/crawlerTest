# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

conn = pymongo.MongoClient('mongodb://localhost')
db = conn['mymongo']
col = db['liepin']


class LiepinPipeline(object):
    def process_item(self, item, spider):
        col.insert({
            'job': item['job'],
            'company': item['company'],
            'salary': item['salary']
        })
        return item
