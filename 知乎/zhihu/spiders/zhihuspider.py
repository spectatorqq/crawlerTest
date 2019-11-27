import json
import scrapy
from copy import deepcopy
from ..items import ZhihuItem
class ZhiHuSpider(scrapy.Spider):
    name = 'zhihu'
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
    }
    cookies = {
        'z_c0' : 'Mi4xTXBGN0J3QUFBQUFBRUdhM1ZrOUlFQmNBQUFCaEFsVk55ZXVuWGdCUUpfNXNzanVNaG9CZ0lTd29YZDh3WlhEV1d3|1572511177|48b7df77a55411ceec5435d891afa9577812b14a'
    }
    infos = ZhihuItem()
    def start_requests(self):
        url = 'https://www.zhihu.com/hot'
        yield scrapy.Request(url=url,headers=self.headers,cookies=self.cookies)
    def parse(self,response):
        titles = response.xpath("//section/div[2]/a/@title").getall()
        urls = response.xpath("//section/div[2]/a/@href").getall()
        for url in urls:
            if 'market' in url or 'special' in url:
                continue
            yield scrapy.Request(url=url,headers=self.headers,cookies=self.cookies,callback=self.parse2,meta={'title':deepcopy(titles[urls.index(url)])})
    def parse2(self,response):
        # 具体问题描述
        q_detail = response.xpath("//div[1]/div[1]/div[2]/div/div/div/span/text()").getall()
        # 高赞回答
        answer = response.xpath("//div[1]/div/div[2]/div[1]/span//text()").getall()
        answer = ''.join(answer)
        title = response.meta['title']
        answer_id = response.xpath("//div[1]/div/@data-zop").getall()[0]
        answer_id = json.loads(answer_id)['itemId']
        url = 'https://www.zhihu.com/api/v4/answers/'+str(answer_id)+'/root_comments?order=normal&limit=10&offset=0&status=open'
        if q_detail:
            yield scrapy.Request(url=url,headers=self.headers,callback=self.parse3,meta={'title':title,'question':deepcopy(q_detail[0]),'answer':answer})
        else:
            yield scrapy.Request(url=url,headers=self.headers,callback=self.parse3,meta={'title':title,'question':' ','answer':answer})
    def parse3(self,response):
        comments = json.loads(response.text)['data']
        comment_str = ''
        for comment in comments:
            comment_str += comment['content']
        self.infos['comments'] = comment_str
        self.infos['question'] = response.meta['question']
        self.infos['title'] = response.meta['title']
        self.infos['answer'] = response.meta['answer']
        yield self.infos


