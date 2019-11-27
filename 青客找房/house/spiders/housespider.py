import scrapy

from day09.house.house.items import HouseItem


class HouseSpider(scrapy.Spider):
    name = 'house'
    city = ['www', 'sz', 'hz', 'bj', 'wh', 'nj']

    def start_requests(self):
        for c in self.city:
            for i in range(1, 393):
                # https: // sz.qk365.com / list
                url = 'https://' + c + '.qk365.com/list/p'+str(i)
                yield scrapy.Request(url=url)
        # yield scrapy.Request(url='https://www.qk365.com/list/p1')

    def parse(self, response):
        city = response.xpath('//div[@class="headLeft"]/div[1]/text()').getall()[0]
        # print(city)
        regions = response.xpath('//ul[@class="easyList"]/li/div[2]/div[1]/div[1]//span').xpath('string(.)').getall()
        advs = response.xpath('//ul[@class="easyList"]/li/div[2]/div[1]/div[1]/p[2]').xpath('string(.)').getall()
        discounts = response.xpath('//ul[@class="easyList"]/li/div[2]/div[1]/div[2]/span/i/text()').getall()
        item = HouseItem()
        for region, adv, discount in zip(regions, advs, discounts):
            item['city'] = city
            item['region'] = region.replace('\n', ' ').replace('\r', ' ').replace(' ', '')
            item['adv'] = adv
            item['discount'] = discount+'元/月'
            yield item
