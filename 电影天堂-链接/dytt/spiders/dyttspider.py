import scrapy
from ..items import DyttItem

class DyttSpider(scrapy.Spider):
    name = 'dytt'
    cate = ['oumei', 'rihan']
    def start_requests(self):
        for c in self.cate:
            # if c == 'china':
            #     for i in range(1, 122):
            #         url = 'https://www.dytt8.net/html/gndy/china/list_4_'+str(i)+'.html'
            #         yield scrapy.Request(url, callback=self.parse)
            if c == 'oumei':
                for i in range(1, 226):
                    url = 'https://www.dytt8.net/html/gndy/oumei/list_7_'+str(i)+'.html'
                    yield scrapy.Request(url, callback=self.parse)

            elif c == 'rihan':
                for i in range(1, 226):
                    url = 'https://www.dytt8.net/html/gndy/oumei/list_8_'+str(i)+'.html'
                    yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        """
        国产电影， 日韩电影， 欧美电影， 分类列表页
        :param response:
        :return:
        """
        urls = response.xpath('//table//tr[2]//td[2]/b/a[2]/@href').getall()    # 每个电影的url
        # print(urls, 'parse')
        for url in urls:
            url = 'https://www.dytt8.net' + url
            yield scrapy.Request(url, callback=self.parse_movie)

    def parse_movie(self, response):
        # file_name = response.xpath('//*[@id="Zoom"]/span/p[1]/text()').getall()[3][5:]
        file_name = response.xpath('//div[@class="title_all"]/h1/font/text()').extract()[0]
        link = response.xpath('//*[@id="Zoom"]//a/@href').getall()[0]
        # translate_name = response.xpath('//*[@id="Zoom"]/span/p[1]/text()').getall()[2][5:]
        # date = response.xpath('//*[@id="Zoom"]/span/p[1]/text()').getall()[4][5:-1]
        # country = response.xpath('//*[@id="Zoom"]/span/p[1]/text()').getall()[5][5:]
        # link = response.xpath('//*[@id="Zoom"]/span/p[1]/a/@href').getall()[0]
        # print(file_name, link)
        item = DyttItem()
        item['film_name'] = file_name
        item['link'] = link
        return item
