from urllib import request as ur
# import urllib.parse
import gzip
from lxml import etree

headers = {
    'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
}
req = ur.Request(url='http://www.xbiquge.la/xiaoshuodaquan/', headers=headers)
res = ur.urlopen(req).read()
# 获取网页
try:
    s = gzip.decompress(res).decode()
except:
    s = res.decode()
# 构建element对象
ele = etree.HTML(s)
# 使用Xpath解析element对象
# 书名列表
books_name = ele.xpath('//div[@class="novellist"]/ul/li/a/text()')
# 书籍链接列表
books_url = ele.xpath('//div[@class="novellist"]/ul/li/a/@href')
# print(books_name)
# print(books_url)
# 遍历两个列表，建立书籍文档名字和进入书籍链接
skip = ['牧神记', '终极斗罗', '全职法师', '人皇纪']
for book_name, book_url in zip(books_name, books_url):
    if book_name in skip:
        continue
    req = ur.Request(url=book_url, headers=headers)
    res = ur.urlopen(req).read()
    try:
        s = gzip.decompress(res).decode()
    except:
        s = res.decode()
    ele = etree.HTML(s)
    chapters_name = ele.xpath('//div[@id="list"]/dl/dd/a/text()')
    chapters_url = ele.xpath('//div[@id="list"]/dl/dd/a/@href')
    print(book_name)
    for chapter_name, chapter_url in zip(chapters_name, chapters_url):
        req = ur.Request(url='http://www.xbiquge.la'+chapter_url, headers=headers)
        res = ur.urlopen(req).read()
        try:
            s = gzip.decompress(res).decode()
        except:
            s = res.decode()
        ele = etree.HTML(s)
        context_list = ele.xpath('//div[@id="content"]/text()')
        c = chapter_name + '\n'
        for context in context_list:
            c += context
        c += '\n'
        with open(book_name+'.txt', mode='a+', encoding='utf8') as f:
            f.write(c)
        print(chapter_name)


