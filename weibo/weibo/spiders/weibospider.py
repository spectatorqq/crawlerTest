from datetime import date
from ..items import WeiboItem
import scrapy
from urllib.parse import urljoin
class WeiboSpiderSpider(scrapy.Spider):
    name = 'weibo'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
    }
    cookies = {
        'SUB': '_2A25wvQw6DeRhGedH6FoW9i_Myj2IHXVTy3ryrDV8PUNbmtAKLUPikW9NUKkSRB3DJPYCy1jXDEhv9Tp2ENUE0IKM'
    }
    hot = WeiboItem()
    # hot['content'] = ''
    # hot['content'] = []
    # hot['num'] = 0
    def start_requests(self):
        url = 'https://s.weibo.com/top/summary'

        yield scrapy.Request(url=url,headers=self.headers,cookies=self.cookies)
    def parse(self,response):
        title = response.xpath("//tr/td[2]/a/text()").getall()
        urls = response.xpath("//tr/td[2]/a/@href").getall()
        for url in urls:
            fullurl = urljoin("https://s.weibo.com",url)
            yield scrapy.Request(url=fullurl,callback=self.parse2,headers=self.headers,cookies=self.cookies,meta={'title':title[urls.index(url)],'rank':urls.index(url)})
    def parse2(self,response):
        content = ''.join(response.xpath("//div[2]/div[2]/div[1]/div[2]/p[1]//text()").getall())
        comment1 = ''.join(response.xpath("//div[2]/div[2]/div[4]/div[2]/div/div[1]/div[2]/div[1]//text()").getall())
        comment2 = ''.join(response.xpath("//div[2]/div[2]/div[4]/div[2]/div/div[2]/div[2]/div[1]//text()").getall())
        self.hot['content'] = str(response.meta['rank'])+content+'\n'+comment1+'\n'+comment2+'\n'
        # self.hot['content'].append((response.meta['rank'],content+'\n'+comment1+'\n'+comment2))
        # self.hot['num']+=1
        yield self.hot

