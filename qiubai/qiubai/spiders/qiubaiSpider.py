# -*- coding: utf-8 -*-
import scrapy
from ..items import QiubaiItem

class QiubaispiderSpider(scrapy.Spider):
    name = 'qiubaiSpider'
    # allowed_domains = ['http://www.lovehhy.net/Joke/Detail/QSBK/']
    # start_urls = ['http://http://www.lovehhy.net/Joke/Detail/QSBK//']
    def start_requests(self):
        pagenum = 1
        while True:
            url ="http://www.lovehhy.net/Joke/Detail/QSBK/"+str(pagenum)
            pagenum += 1
            yield scrapy.Request(url=url)

    def parse(self, response):
        title = response.xpath("//h3/a/text()").getall()
        cont = response.xpath("//div[@id='endtext']").getall()

        cont_1 = [i.replace('<div id="endtext">','').replace('<br>','').replace('</div>','') for i in cont]
        print(title, cont_1)
        item = QiubaiItem()
        item['title'] = title
        item['cont'] = cont_1
        # print(urls)
        # for url in urls:
        #     url='http://www.lovehhy.net'+url
        #     yield scrapy.Request(url=url,callback=self.parse1)

    # def parse1(self,response):
    #     title = response.xpath("//h1/text()").getall()[0]
    #     cont = response.xpath("//div[@id='fontzoom']/text()").getall()
    #
    #     c=''
    #     for i in cont:
    #         c+=i.strip()
    #     item = QiubaiItem()
    #     print(title, c)
    #     item['title']=title
    #     item['cont']=c
    #     yield item