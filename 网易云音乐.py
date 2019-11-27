# from selenium import webdriver
# import MySQLdb
# # import time
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# web = webdriver.Chrome(r'F:\Zpark\python crawler\self_code\day10\chromedriver.exe', chrome_options=chrome_options)
#
# web.get(url='https://music.163.com/#/song?id=1363948882')
# # time.sleep(2)
# web.switch_to.frame('g_iframe')
# # web.implicitly_wait(6)
# # js = "var q=document.documentElement.scrollTop=10000"
# # web.execute_script(js)
# # web.execute_script("window.scrollBy(0,10000)")
# conn = MySQLdb.connect(host='localhost', port=3306, user='root', password='123456', db='crawler', charset='utf8')
# cursor = conn.cursor()
# num = 1
# while 1:
#     divs = web.find_elements_by_xpath("//div[@class='itm']/div[2]/div[1]")
#     print(num)
#     num += 1
#     for d in divs:
#         print(d.text)
#         try:
#             sql = 'insert into 163comments values(%s)'
#             cursor.execute(sql, (str(d.text), ))
#         except:
#             continue
#     conn.commit()
#     web.implicitly_wait(3)
#     next_p = web.find_element_by_xpath('//a[text()="下一页"]')
#     web.execute_script('arguments[0].click();', next_p)

import jieba
import wordcloud
import numpy as np
from PIL import Image
import MySQLdb

conn = MySQLdb.connect(host='localhost', port=3306, user='root', password='123456', db='crawler', charset='utf8')
cursor = conn.cursor()
words = []
cursor.execute('select * from 163comments')
res = cursor.fetchall()
for r in res:
    com = r[0].split('：', 1)[1].replace('，', '').replace('\n', '')
    words += jieba.lcut(com)
    # words.extend(ws)
print(words)
img = np.array(Image.open('F:\Zpark\python crawler\self_code\day11\\1533889105927_55.png'))

wcloud = wordcloud.WordCloud(font_path='FZSTK.TTF', scale=4,
                             background_color='white',
                             mask=img)
wcloud.generate(" ".join(words))
wcloud.to_file('环环2.jpg')
