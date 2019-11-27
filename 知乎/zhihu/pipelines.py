# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
conn = pymongo.MongoClient("mongodb://localhost:27017")
mydb = conn['test1']
myset = mydb['zhihu']

class ZhihuPipeline(object):
    def process_item(self, item, spider):
        myset.insert({'title':item['title'],'question':item['question'],'answer':item['answer'],'comment':item['comments']})
        return item
