import requests
from lxml import etree
import re
start = 0
while start<100:
    url = "https://www.pearvideo.com/popular_loading.jsp?reqType=1&start="+str(start)
    start+=10
    res = requests.get(url).text
    ele = etree.HTML(res)
    urls = ele.xpath("//li/a/@href")
    for url in urls:
        res = requests.get("https://www.pearvideo.com/"+url).text
        ele = etree.HTML(res)
        name = ele.xpath("//h1/text()")[0]
        url = re.compile('http.*mp4').findall(res)[0]
        res = requests.get(url).content
        with open(name+".mp4",'wb') as f:
            f.write(res)
        print(name,url)
        exit()