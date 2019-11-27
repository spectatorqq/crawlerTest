# -*- coding: utf-8 -*-
import scrapy


class WeathercnSpider(scrapy.Spider):
    name = 'weathercn'
    # allowed_domains = ['www.weather.com.cn']
    start_urls = ['http://www.weather.com.cn/forecast/']

    def parse(self, response):
        urls = response.xpath('//div[@class="maptabboxinBox"]/div/h4/a/@href').getall()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_district)

    def parse_district(self, response):
        urls = response.xpath('//div[@class="hanml"]/div[1]/div/table/tr[position()>2]/td[@width="83"]/a/@href').getall()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_city)

    def parse_city(self, response):
        city = response.xpath('/html/body/div[5]/div[1]/div[1]/div[1]/div[1]/a[last()]/text()').getall()[0]
        if city in ['北京', '天津', '上海', '重庆']:
            city += response.xpath('/html/body/div[5]/div[1]/div[1]/div[1]/div[1]/span[last()]/text()').getall()[0]
        days = response.xpath('//*[@id="7d"]/ul/li')
        for day in days:
            date = day.xpath('./h1/text()').getall()[0].strip()[:-4]
            weather = day.xpath('./p[1]/@title').getall()[0].strip()
            temperature = day.xpath('./p[2]')[0].xpath('string(.)').extract()[0].strip()
            wind_direction = ','.join(day.xpath('./p[3]/em/span/@title').getall()).strip()
            wind_level = day.xpath('./p[3]/i/text()').getall()[0].strip()
            print(city, date, weather, temperature, wind_direction, wind_level)
