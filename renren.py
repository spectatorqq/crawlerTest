import requests
from lxml import etree
import MySQLdb
from chaojiying import chaojiying_check
# import time
conn = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    db='crawler',
    charset='utf8'
)
cursor = conn.cursor()

headers = {
    'Cookie': 'anonymid=k2jp0koh-z48a9u; depovince=GW; _r01_=1; JSESSIONID=abcuY5b9ASsXueB1M1Z4w; ick_login=b780f0e4-aaa0-4a4a-90b1-8cb2fe067171; ick=65114014-db6f-407b-8a74-829fbe26f089; t=4ced2d7024376ea767346874ab93a8808; societyguester=4ced2d7024376ea767346874ab93a8808; id=972774708; xnsid=cc2891a8; ver=7.0; loginfrom=null; jebe_key=7e9b1055-c10d-42a6-af4d-efd3bac17828%7C4b34b58511736865d0406047c56ac39f%7C1572827949500%7C1%7C1572827952279; jebe_key=7e9b1055-c10d-42a6-af4d-efd3bac17828%7C4b34b58511736865d0406047c56ac39f%7C1572827949500%7C1%7C1572827952281; wp_fold=0; XNESSESSIONID=2532567c0d10; jebecookies=7dcabbb0-0c43-4f8b-aa4a-5df63fc76ff5|||||'
}


def focus():
    for i in range(25):
        res = requests.get(url='http://page.renren.com/600217117/channel-fanslist?curpage='+str(i), headers=headers)
        html = res.text
        ele = etree.HTML(html)
        fans_url = ele.xpath('//ul[@class="clearfix"]/li/div/a/@href')
        fan_sql = 'insert user_url values(%s, %s)'
        lst = [[url[-9:], '0'] for url in fans_url]
        cursor.executemany(fan_sql, lst)
        conn.commit()


def get_footprint_url():
    url = 'http://www.renren.com/943590643/profile'
    res = requests.get(url=url, headers=headers)
    html = res.text
    ele = etree.HTML(html)
    visiters_url = ele.xpath('//*[@id="footprint-box"]/ul/li/a/@href')
    print(visiters_url)


def user_info():
    """
    从数据库里查没有访问过的url，在TA的个人主页找到名字， 其他信息，和看过他的人的url，获取该人的id
    :return:
    """
    query_sql = 'select * from user_url where status="0"'
    if cursor.execute(query_sql):
        url_tuple = cursor.fetchall()
        for url, status in url_tuple:
            # 看完一个人就将他的url的状态变为 1
            update_sql = 'update user_url set status="1" where url='+'"'+url+'"'
            cursor.execute(update_sql)
            user_id = url
            cookies = {
                't': '4ced2d7024376ea767346874ab93a8808'
            }
            url = 'http://www.renren.com/'+user_id+'/profile'
            res = requests.get(url=url, cookies=cookies)
            html = res.text
            ele = etree.HTML(html)
            # print(html)
            try:
                name = ele.xpath('//title/text()')[0]    # 我的名字
            except:
                continue
            name = name[6:]
            if '验证码' in name:
                code_url = ele.xpath('//div[@class="optional"]/img/@src')[0]
                code = requests.get(code_url, cookies=cookies)
                result = chaojiying_check(code.content)
                print(result)
                pic_str = result['pic_str']
                data = {
                    'id': user_id,
                    'icode': pic_str,
                    'submit': '继续浏览',
                    'requestToken': '1625924297',
                    '_rtk': '2caaa123'
                }
                res = requests.post(url='http://www.renren.com/validateuser.do', data=data, cookies=cookies)
                # print(res.text)
                continue
            info = ele.xpath('//div[@class="tl-information"]/ul/li//text()')    # 我的信息
            visiters_url = ele.xpath('//*[@id="footprint-box"]/ul/li/a/@href')  # 谁看过我
            msg = ''
            for s in info:
                msg += s + '\t'
            print(name, msg)
            add_sql = 'insert renren_user values(%s, %s)'
            v_url_sql = 'insert user_url values(%s, %s)'
            # 将用户信息加入到数据库
            cursor.execute(add_sql, (name, msg))
            # 将新的url加入数据库

            for v in visiters_url:
                try:
                # 避免是个空的足迹信息
                # 避免重复时停止程序
                    cursor.execute(v_url_sql, (v[-9:], '0'))
                except:
                    pass
                # 所有操作统一提交
            conn.commit()


def test():
    url = 'http://www.renren.com/943590643/profile'
    res = requests.get(url, headers=headers)
    print(res.text)

# for fan_url in fans_url:
#     res = requests.get(url=fan_url, headers=headers)
#     html = res.text
#     ele = etree.HTML(html)
#     print(html)
#     # name = ele.xpath('//*[@id="cover"]/div[2]/h1/text()')
#     # info = ele.xpath('//div[@class="tl-information"]/ul/li/text()')
#     # print(name)
#     # print(info)
#     time.sleep(0.3)


if __name__ == '__main__':
    # focus()
    while 1:
        user_info()
    # # test()
    # # get_footprint_url()
