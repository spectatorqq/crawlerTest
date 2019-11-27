import scrapy

from day11.liepin.liepin.items import LiepinItem


class LieSpider(scrapy.Spider):
    name = 'liepin'
    position = ['全栈工程师', '自然语言处理', '新媒体运营', '记者', '文案策划']

    def start_requests(self):
        # url = 'https://www.liepin.com/it/?mscid=s_00_pz0&utm_source=baidu&utm_medium=cpc&utm_campaign=%E6%90%9C%E7%B4%A2&utm_content=%E8%A1%A8%E6%A0%BC&utm_term=%E5%88%973'
        url = 'https://www.liepin.com/financial/?mscid=s_00_pz0&utm_source=baidu&utm_medium=cpc'
        yield scrapy.Request(url)

    def parse(self, response):
        # positions = response.xpath('//a[@rel="nofollow"]/text()').getall()[:133]
        positions = response.xpath('//a[@rel="nofollow"]/text()').getall()
        # for i in enumerate(positions):
        #     print(i)
        # for i in range(len(positions)-1, 0, -1):
        #     print(positions[i])
        for i in range(2, len(positions)):
            for p in range(100):
                # print(positions[i], p)
                # url = 'https://www.liepin.com/zhaopin/?init=-1&headckid=3412f26fa94f3926&fromSearchBtn=2' \
                #       '&imscid=R000000035' \
                #       '&ckid=c9e30cd2109d7358&degradeFlag=0&key='+positions[i] + \
                #       '&siTag=8mPLiCdWAdX8Ns0b4TqhAA%7EfA9rXquZc5IkJpXC-Ycixw&d_sfrom=search_unknown&' \
                #       'd_ckId=4477ca9a9c1e45350129d522489ca415&d_headId=33ecfd157368ccd18d9e461f75f5846e&curPage='+\
                #       str(p)
                url = 'https://www.liepin.com/zhaopin/?init=-1&headckid=3f3ed3949a7988e3&dqs=&fromSearchBtn=2&' \
                      'imscid=R000000037&ckid=b46633038d703f85&degradeFlag=0&key='+positions[i] +\
                      '&siTag=vYOdsNXZUTRv3A0jWBEDmw%7EfA9rXquZc5IkJpXC-Ycixw&d_sfrom=search_sub_site' \
                      '&d_ckId=fce8c2ec012de38f2d92325ea2523294&d_curPage=0&d_pageSize=40' \
                      '&d_headId=6edf6cdd0f64abba57606d5c5ebca164&curPage='+str(p)
                yield scrapy.Request(url, callback=self.parse2)
            # break

    def parse2(self, response):
        print('parse2')
        jobs = response.xpath('//div[@class="sojob-item-main clearfix"]/div[1]/h3/a/text()').getall()
        salaries = response.xpath('//div[@class="sojob-item-main clearfix"]/div[1]/p[1]/span[1]/text()').getall()
        companies = response.xpath('//p[@class="company-name"]/a/text()').getall()
        item = LiepinItem()
        for job, salary, company in zip(jobs, salaries, companies):
            item['job'] = job.strip()
            item['company'] = company
            item['salary'] = salary
            yield item
