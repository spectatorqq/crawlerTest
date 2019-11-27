import requests
from lxml import etree


# headers = {
#     'User-Agent': 'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
#     'Referer': 'https://www.guazi.com/www/buy/c-1l2/',
#     'Cookie': 'track_id=3268210380312576; uuid=2fe271fb-ed86-47d2-897b-0e9230210e25; antipas=I602ukQ746296R5623371198; clueSourceCode=10103000312%2300; ganji_uuid=4521411913003474738283; sessionid=fd192698-fa18-4bf8-df3f-11a57ced8392; lg=1; cainfo=%7B%22ca_a%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_s%22%3A%22pz_baidu%22%2C%22ca_n%22%3A%22tbmkbturl%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22%22%2C%22ca_campaign%22%3A%22%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%2210103000312%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22ca_transid%22%3A%22%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22track_id%22%3A%223268210380312576%22%2C%22display_finance_flag%22%3A%22-%22%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%222fe271fb-ed86-47d2-897b-0e9230210e25%22%2C%22ca_city%22%3A%22tj%22%2C%22sessionid%22%3A%22fd192698-fa18-4bf8-df3f-11a57ced8392%22%7D; _gl_tracker=%7B%22ca_source%22%3A%22-%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A1702754634%7D; user_city_id=-1; preTime=%7B%22last%22%3A1571934624%2C%22this%22%3A1571934402%2C%22pre%22%3A1571934402%7D; cityDomain=gz'
# }
# proxy = {
#     'http': '183.91.33.42:8085'
# }
# res = requests.get(url='https://www.guazi.com/www/buy/c-1l2h2/', headers=headers, proxies=proxy)
# print(res.content.decode())

index_url = 'https://quanguo.58.com/yeuyeche/pve_5883_2016_2018/?/'
index_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'https://quanguo.58.com/ershouche/',
}

# index_response = requests.get(url=index_url, headers=index_headers)
# res = index_response.text
# # print(res)
# ele = etree.HTML(res)
# # car_name = ele.xpath('//td[@class="t"]/a/font/text()')
# car_info = ele.xpath('//td[@class="t"]/p/text()')
# # print(car_name)
for i in range(2, 20):
    url = 'https://quanguo.58.com/yeuyeche/pn'+str(i)+'/pve_5883_2016_2018/?'
    index_response = requests.get(url=url, headers=index_headers)
    res = index_response.text
    # print(res)
    ele = etree.HTML(res)
    car_names = ele.xpath('//td[@class="t"]/a/font/text()')
    car_types = ele.xpath('//td[@class="t"]/a/text()')
    info = ele.xpath('//td[@class="t"]/p/text()')
    prices = ele.xpath('//td[@class="tc"]/b/text()')
    # print(len(car_names), car_names)
    for car_name, car_type, price, j in zip(car_names, car_types, prices, range(0, int(len(info)/4), 3)):
        msg = ''
        buy_data = info[4 * j + 0].strip()      # 购买时间
        mileage = info[4 * j + 1].strip()       # 里程数
        discharge = info[4 * j + 2].strip()     # 排量
        gear_type = info[4 * j + 3].strip()     # 自动挡、手动挡
        msg += car_name + ',' + car_type+','+price+'万元'+","+buy_data+','+mileage+','+discharge+','+gear_type+'\n'
        with open('58二手车SUV.text', 'a+', encoding='utf8') as f:
            f.write(msg)
        print(msg)
