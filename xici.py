from urllib import request as ur
import time
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
    # 'User-Agent': 'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
}

number = 1
while 1:
    req = ur.Request(url='https://www.xicidaili.com/wn/'+str(number), headers=headers)
    number += 1
    res = ur.urlopen(req).read()
    res = res.decode()
    # print(res)
    ele = etree.HTML(res)
    # ips = ele.xpath('//table')
    ips = ele.xpath('//table//tr[position()>1]/td[2]/text()')
    ports = ele.xpath('//table//tr[position()>1]/td[3]/text()')
    print('ips', ips)
    for ip in ips:
        proxy_ip = {
            'https': ip
        }
        handler = ur.ProxyHandler(proxies=proxy_ip)
        opener = ur.build_opener(handler)
        try:
            time.sleep(1)
            res = opener.open(fullurl='https://www.httpbin.org/ip', timeout=8)
        except :
            print('超时')
            continue
        res = res.read().decode()

        if '111.33.3.82' not in res and '111.33.3.90' not in res and 'unknown' not in res:
            number += 1
            print('number:', number)
            print(res)
            with open('https_xi_ci.txt', 'a+', encoding='utf8') as f:
                # f.write(ip+','+port+','+ip_type+'\n')
                f.write('https'+'://'+ip+"\n")
