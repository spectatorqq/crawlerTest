import scrapy
import json

from day06_source_code.zhilian.zhilian.items import ZhilianItem

# cityid = {
#     '深圳': 765, '北京': 530, '上海': 538, '广州': 763, '西安': 854, '重庆': 551,'天津': 531,
#     '成都': 801, '杭州': 653,
# }
cityid = [765, 530, 538, 763, 854, 551, 531, 801, 653, 736, 600, 613, 635, 702, 719, 749,
          622, 636, 654, 681, 682, 565, 664, 773, 565, 571, 568, 573, 575, 570, 585, 580,
          577, 588, 659, 599, 803, 800, 857, 822, 787, 831, 843, 720, 721, 734, 691, 728,
          750, 760, 752]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
}

class ZhilianSpider(scrapy.Spider):
    name = 'zhilian'

    def start_requests(self):
        for c in cityid:
            for i in range(90, 991, 90):
                url = 'https://fe-api.zhaopin.com/c/i/sou?start='+str(i)+'&pageSize=90&cityId='+str(c)+'&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E9%94%80%E5%94%AE%E4%BB%A3%E8%A1%A8&kt=3&=0&_v=0.67409609&x-zp-page-request-id=04622f5a133e489b8c7b42b9c5a1f4e9-1572349219862-499472&x-zp-client-id=76250214-3ba6-4629-817c-930168092ab8'
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # print(response.text)
        data = json.loads(response.text)['data']
        results = data['results']
        item = ZhilianItem()
        items = item['items'] = []
        for i in results:
            job = i['jobName']
            grade = i['eduLevel']['name']
            experience = i['workingExp']['name']
            salary = i['salary']
            info = [job, grade, experience, salary]
            items.append(info)
            # item['job'] = job
            # item['grade'] = grade
            # item['experience'] = experience
            # item['salary'] = salary
        yield item 

