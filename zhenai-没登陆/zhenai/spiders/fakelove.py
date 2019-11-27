import scrapy

from day07.zhenai.zhenai.items import ZhenaiItem


class FakeSpider(scrapy.Spider):
    name = 'fake_love'

    def start_requests(self):
        url = 'http://www.zhenai.com/zhenghun'
        yield scrapy.Request(url=url)

    def parse(self, response):
        urls = response.xpath('//dl[@class="city-list clearfix"]/dd/a/@href').getall()
        print(urls)
        for url in urls:
            for i in range(1, 7):
                url += '/' + str(i)
                yield scrapy.Request(url=url, callback=self.parse1)

    def parse1(self, response):
        nick_names = response.xpath('//div[@class="list-item"]/div[2]/table/tbody/tr[1]/th/a/text()').getall()
        genders = response.xpath('//div[@class="list-item"]/div[2]/table/tbody/tr[2]/td[1]/text()').getall()
        ages = response.xpath('//div[@class="list-item"]/div[2]/table/tbody/tr[3]/td[1]/text()').getall()
        places = response.xpath('//div[@class="list-item"]/div[2]/table/tbody/tr[2]/td[2]/text()').getall()
        item = ZhenaiItem()
        items = item['fake_love'] = []
        for nick_name, gender, age, place in zip(nick_names, genders, ages, places):
            info = [nick_name, gender, age, place]
            items.append(info)
        yield item
