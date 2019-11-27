# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import date

class WeiboPipeline(object):
    def process_item(self, item, spider):
        # item['content'].sort()
        # cont = sorted(item['content'])
        # cont = ''.join([str(i[0])+i[1] for i in cont])
        # # print(cont)
        with open(date.today().strftime("%Y-%m-%d")+'.txt','a+',encoding='utf-8') as f:
            # f.write(cont)
            f.write(item['content'])
        return item
