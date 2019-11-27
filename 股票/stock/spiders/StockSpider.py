import scrapy
import json
from ..items import StockItem
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
    'Cookie': 'qgqp_b_id=7e985e7f767bdf10b5cb7a5c32e6c42f; st_si=03149943099215; st_asi=delete; st_pvi=87903044782019; st_sp=2019-11-01%2017%3A10%3A20; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink; st_sn=3; st_psi=20191101171124761-113200301321-0343712494'
}


class StockSpider(scrapy.Spider):
    name = 'stock'

    def start_requests(self):
        for i in range(1, 39):
            url = 'http://22.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124009509785844729546_1572599484232&pn='+str(i)+'&pz=100&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:13,m:0+t:80,m:1+t:2,m:1+t:23&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1572599484266'

            yield scrapy.Request(url=url, headers=headers)

    def parse(self, response):
        context = response.text[43:-2]
        json_data = json.loads(context)
        data = json_data['data']
        diff = data['diff']
        item = StockItem()
        for d in diff:
            code = d['f12']
            name = d['f14']
            last_price = d['f2']
            deal_price = d['f6']
            pe_ratio = d['f9']
            item['code'] = code
            item['name'] = name
            item['last_price'] = last_price
            item['deal_price'] = deal_price
            item['pe_ratio'] = pe_ratio
            yield item

