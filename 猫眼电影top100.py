import time
from urllib import request as ur
from lxml import etree
from MySQLdb import connect
# import gzip
# res = ''

conn = connect(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    db='crawler',
    charset='utf8'
)

cursor = conn.cursor()


films_name = []
films_url = []

headers = {
    'User-Agent': 'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
    # 'User_Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.6 (KHTML, like Gecko) Chrome/7.0.500.0 Safari/534.6Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    # 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'
    # 'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}

for i in range(0, 100, 10):
    req = ur.Request(url='https://maoyan.com/board/4?offset='+str(i), headers=headers)
    res = ur.urlopen(req)
    res = res.read().decode()
    ele = etree.HTML(res)
    films_name += ele.xpath('//p[@class="name"]/a/text()')
    films_url += ele.xpath('//p[@class="name"]/a/@href')
# print(films_name)
# print(films_url)

for film_url, film_name in zip(films_url, films_name):
    req = ur.Request(url='https://maoyan.com'+film_url, headers=headers)
    time.sleep(0.01)
    res = ur.urlopen(req)
    res = res.read().decode()
    ele = etree.HTML(res)
    # print(res)
    c_file_name = ele.xpath('//div[@class="movie-brief-container"]/h3[@class="name"]/text()')[0]
    e_file_name = ele.xpath('//div[@class="movie-brief-container"]/div[@class="ename ellipsis"]/text()')[0]
    lis_text = ele.xpath('//div[@class="movie-brief-container"]/ul/li[@class="ellipsis"]/text()')
    film_type = lis_text[0]
    country = lis_text[1].split('/')[0].strip()
    duration = lis_text[1].split('/')[1].strip()
    release_date = lis_text[2][:10]
    release_site = lis_text[2][10:-2]
    print(c_file_name, e_file_name, lis_text)
    with open('猫眼电影top100.txt', mode='a+', encoding='utf8') as f:
        f.write(c_file_name+','+e_file_name+','+film_type+','+release_site+','+release_date+','+
                duration+','+country+'\n')
        # print(c_file_name)
    print(c_file_name)
    sql = 'insert into maoyanfilmtop100(c_file_name,e_file_name, duration, release_date, release_site, film_type, country)' \
          ' values(%s,%s,%s,%s,%s,%s,%s)'
    cursor.execute(sql, (c_file_name, e_file_name, duration, release_date, release_site, film_type, country))
conn.commit()
cursor.close()
conn.close()
