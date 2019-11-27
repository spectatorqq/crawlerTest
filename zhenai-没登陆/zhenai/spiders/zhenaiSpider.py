import time

import scrapy
import json

headers = {
    'referer': 'https://www.zhenai.com/n/search',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
}
cookies = {
    'token': '1708846120.1572429154803.92a67f7f2fe3ab51eff400ab945b37e4'

}


class ZhenaiSpider(scrapy.Spider):
    name = 'zhenai'

    def start_requests(self):
        page = 1
        while True:
            data = {
                'sex': '1',
                'workCity': '-1',
                'ageBegin': '-1',
                'ageEnd': '-1',
                'heightBegin': '-1',
                'heightEnd': '-1',
                'body': '-1',
                'multiEducation': '-1',
                'salaryBegin': '-1',
                'salaryEnd': '-1',
                'page': str(page),
                'pageSize': '100',
                '_': '1572427370975',
                'ua': 'h5/1.0.0/1/0/0/0/901045/0//0/0/3765bf30-a3ee-4c2d-a176-da0a8635100d/0/0/394476254',
            }
            url = 'https://www.zhenai.com/api/search/getConditionData.do'
            yield scrapy.FormRequest(url=url, formdata=data, headers=headers, cookies=cookies)
            time.sleep(0.5)
            page += 1

    def parse(self, response):
        print(response.text)
