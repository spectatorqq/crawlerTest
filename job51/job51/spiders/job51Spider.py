import scrapy
from ..items import Job51Item


class Job51Spider(scrapy.Spider):
    name = 'job51'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
    }

    def start_requests(self,):
        for i in range(1, 2000):
            url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,%25E9%2594%2580%25E5%2594%25AE,2,'+str(i)+'.html'
            yield scrapy.Request(url=url,)

    def parse(self, response):
        job_urls = response.xpath('//div[ @ id = "resultList"]/div[@class="el"]/p/span/a/@href').getall()
        for url in job_urls:
            yield scrapy.Request(url=url, callback=self.parse_url, headers=self.headers)
        # jobs = response.xpath('//div[ @ id = "resultList"]/div[@class="el"]/p/span/a/text()').getall()
        # companies = response.xpath('//div[ @ id = "resultList"]/div[@class="el"]/span[1]/a/text()').getall()
        # work_places = response.xpath('//div[ @ id = "resultList"]/div[@class="el"]/span[2]/text()').getall()
        # salaries = response.xpath('//div[ @ id = "resultList"]/div[@class="el"]/span[3]/text()').getall()
        # item = Job51Item()
        # for job, company, work_place, salary in zip(jobs, companies, work_places, salaries):
        #     item['job'] = job.strip()
        #     item['company'] = company
        #     item['work_place'] = work_place
        #     item['salary'] = salary
        #     # print(item)
        #     yield item

    def parse_url(self, response):
        job = response.xpath('//div[@class="cn"]/h1/text()').getall()[0]
        salary = response.xpath('//div[@class="cn"]/strong/text()').getall()
        if len(salary) == 0:
            salary = '暂无'
        else:
            salary = salary[0]
        company = response.xpath('//div[@class="cn"]/p[@class="cname"]/a[1]/text()').getall()[0].strip()
        work_place = response.xpath('//div[@class="cn"]/p[@class="msg ltype"]/text()').getall()[0].strip()
        item = Job51Item()
        item['job'] = job.strip()
        item['company'] = company
        item['work_place'] = work_place
        item['salary'] = salary
        # print(item)
        yield item
