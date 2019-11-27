import requests
from lxml import etree


for i in range(10):
    url = 'https://movie.douban.com/subject/30402296/photos?type=S&start={}&sortby=like&size=a&subtype=a'.format(i * 30)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
        'Cookie': ''
    }
    html = requests.get(url=url).text
    ele_html = etree.HTML(html)
    imgs = ele_html.xpath("//ul[@class='poster-col3 clearfix']//div[@class='cover']/a/@href")
    for j in imgs:
        img_detail = requests.get(url=j, headers=headers).text
        ele_detail = etree.HTML(img_detail)
        original = ele_detail.xpath("//span[@class='update magnifier']/a/@href")
        headers['Referer'] = url
        print(original[0].rsplit('/', 1)[-1])
        res = requests.get(url=original[0], headers=headers)
        with open('C:/Users/HIAPAD/Desktop/天气之子/' + original[0].rsplit('/', 1)[-1], 'wb') as i:
            i.write(res.content)
