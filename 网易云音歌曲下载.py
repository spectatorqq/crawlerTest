import requests
from lxml import etree

# 网易云歌曲一般会有一个外链，专门用于下载音乐音频的，以赵雷的歌曲《成都》为例，《成都》的外链URL是：
# http://music.163.com/song/media/outer/url?id=436514312.mp3
headers = {
'referer': 'https://music.163.com/',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
}
url='https://music.163.com/discover/toplist'
res=requests.get(url=url,headers=headers).text
# print(res)

ele = etree.HTML(res)
ids = ele.xpath("//ul[@class='f-hide'][1]/li/a/@href")
name = ele.xpath("//ul[@class='f-hide'][1]/li/a/text()")
# print(ids)
# print(name)

download_url = 'http://music.163.com/song/media/outer/url?id={}.mp3'
for i in range(len(ids)):
    print(name[i],'    ',ids[i].split('=')[1])
    res = requests.get(download_url.format(ids[i].split('=')[1]))
    with open(name[i]+'.mp3','wb') as w:
        w.write(res.content)
    break