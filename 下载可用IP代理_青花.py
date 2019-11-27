from urllib import request as ur
import time
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
    # 'User-Agent': 'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
}

ip_agents = {}
# agent_urls = []
number = 0
for i in range(1, 100):
    req = ur.Request(url='http://qinghuadaili.com/free/'+str(i)+'/', headers=headers)
    res = ur.urlopen(req).read()
    # print(res.decode())
    ele = etree.HTML(res.decode())
    ips = ele.xpath('/html/body/div/div/div/div[2]/table/tbody/tr/td[1]/text()')
    ports = ele.xpath('/html/body/div/div/div/div[2]/table/tbody/tr/td[2]/text()')
    types = ele.xpath('/html/body/div/div/div/div[2]/table/tbody/tr/td[4]/text()')
    print(ips)
    print(ports)
    print(types)
    for ip, ip_type, port in zip(ips, types, ports):
        proxy_ip = {
            'http': ip+':'+port
        }
        handler = ur.ProxyHandler(proxies=proxy_ip)
        opener = ur.build_opener(handler)
        try:
            time.sleep(1)
            res = opener.open(fullurl='http://www.httpbin.org/ip', timeout=8)
        except :
            print('超时')
            continue
        res = res.read().decode()

        if '111.33.3.82' not in res and '111.33.3.90' not in res and 'unknown' not in res:
            number += 1
            print('number:', number)
            print(res)

            ip_agents.setdefault(ip_type, ip+':'+port)
            with open('ip_agents.txt', 'a+', encoding='utf8') as f:
                # f.write(ip+','+port+','+ip_type+'\n')
                f.write(ip_type+'://'+ip+":"+port+"\n")
