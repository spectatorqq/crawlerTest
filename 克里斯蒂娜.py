from urllib import request as ur
import re
# https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E7%89%A7%E6%BF%91%E7%BA%A2%E8%8E%89%E6%A0%96+%E5%A4%B4%E5%83%8F&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&word=%E7%89%A7%E6%BF%91%E7%BA%A2%E8%8E%89%E6%A0%96+%E5%A4%B4%E5%83%8F&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&expermode=&force=&pn=60&rn=30&gsm=&1571824888041=
# https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E7%89%A7%E6%BF%91%E7%BA%A2%E8%8E%89%E6%A0%96+%E5%A4%B4%E5%83%8F&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&word=%E7%89%A7%E6%BF%91%E7%BA%A2%E8%8E%89%E6%A0%96+%E5%A4%B4%E5%83%8F&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&expermode=&force=&pn=30&rn=30&gsm=&1571824887885=
pic_urls = []
headers = {
    'Accept': 'text / plain, * / *;q = 0.01',
    'Accept - Encoding': 'gzip, deflate, br',
    'Accept - Language': 'zh - CN, zh;q = 0.9, en;q = 0.8',
    'Connection': 'keep - alive',
    'Cookie': 'BDqhfp = % E7 % 89 % A7 % E6 % BF % 91 % E7 % BA % A2 % E8 % 8,E % 89 % E6 % A0 % 96 % 26 % 26 - 10 - 1 undefined % 26 % 26575 % 26 % 262;BAIDUID = 7 F08A76C65C8305D9A8F7487FB2B54FE: FG = 1; BIDUPSID = 7 F08A76C65C8305D9A8F7487FB2B54FE;PSTM = 1561203409;__cfduid = dbd7c6d215349414362b14cea44830b891562765319;BDUSS = VAxR3R6bHY2cUVVUzJYS2JqVU9YbFU3TFA3VlQzdndBN2xXdEwxVWU0YndrbEpkRVFBQUFBJCQAAAAAAAAAAAEAAAABoVSZzfzV39ChxqYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPAFK13wBStde;BDORZ = B490B5EBF6F3CD402E515D22BCDA1598;MCITY = -332 % 3A;indexPageSugList = % 5B % 22 % E7 % 89 % A7 % E6 % BF % 91 % E7 % BA % A2 % E8 % 8E % 89 % E6 % A0 % 96 % 22 % 5D;H_PS_PSSID = 1464_21112_29911_29567_29220;delPer = 0;PSINO = 5;BDRCVFR[dG2JNJb_ajR] = mk3SLVN4HKm;userFrom = www.baidu.com;BDRCVFR[-pGxjrCMryR] = mk3SLVN4HKm;cleanHistoryStatus = 0',
    'Host': 'image.baidu.com',
    'Referer': 'https: // image.baidu.com / search / index?tn = baiduimage & ipn = r & ct = 201326592 & cl = 2 & lm = -1 & st = -1 & fm = result & fr = & sf = 1 & fmq = 1571877057969_R & pv = & ic = & nc = 1 & z = & hd = & latest = & copyright = & se = 1 & showtab = 0 & fb = 0 & width = & height = & face = 0 & istype = 2 & ie = utf - 8 & sid = & word = % E7 % 89 % A7 % E6 % BF % 91 % E7 % BA % A2 % E8 % 8E % 89 % E6 % A0 % 96Sec - Fetch - Mode: corsSec - Fetch - Site: same - origin',
    'User - Agent': 'Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 77.0.3865.120Safari / 537.36',
    'X - Requested - With': 'XMLHttpRequest'}

# def decode_url(url):
#     """
#     对百度加密后的地址进行解码\n
#     :param url:百度加密的url\n
#     :return:解码后的url
#     """
#     table = {'w': "a", 'k': "b", 'v': "c", '1': "d", 'j': "e", 'u': "f", '2': "g", 'i': "h",
#              't': "i", '3': "j", 'h': "k", 's': "l", '4': "m", 'g': "n", '5': "o", 'r': "p",
#              'q': "q", '6': "r", 'f': "s", 'p': "t", '7': "u", 'e': "v", 'o': "w", '8': "1",
#              'd': "2", 'n': "3", '9': "4", 'c': "5", 'm': "6", '0': "7",
#              'b': "8", 'l': "9", 'a': "0", '_z2C$q': ":", "_z&e3B": ".", 'AzdH3F': "/"}
#     url = re.sub(r'(?P<value>_z2C\$q|_z\&e3B|AzdH3F+)', lambda matched: table.get(matched.group('value')), url)
#     return re.sub(r'(?P<value>[0-9a-w])', lambda matched: table.get(matched.group('value')), url)


def baidtu_uncomplie(url):
    res = ''
    c = ['_z2C$q', '_z&e3B', 'AzdH3F']
    d= {'w':'a', 'k':'b', 'v':'c', '1':'d', 'j':'e', 'u':'f', '2':'g', 'i':'h', 't':'i', '3':'j', 'h':'k', 's':'l', '4':'m', 'g':'n', '5':'o', 'r':'p', 'q':'q', '6':'r', 'f':'s', 'p':'t', '7':'u', 'e':'v', 'o':'w', '8':'1', 'd':'2', 'n':'3', '9':'4', 'c':'5', 'm':'6', '0':'7', 'b':'8', 'l':'9', 'a':'0', '_z2C$q':':', '_z&e3B':'.', 'AzdH3F':'/'}
    if(url==None or 'http' in url):
        return url
    else:
        j= url
        for m in c:
            j=j.replace(m,d[m])
        for char in j:
            if re.match('^[a-w\d]+$',char):
                char = d[char]
            res= res+char
        return res


opener = ur.build_opener()
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'),('Referer','http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1571880512755_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&sid=&word=%E6%9D%A8%E8%8C%9C%E6%B7%B3')]
ur.install_opener(opener)
for i in range(30, 220, 30):
    req = ur.Request(url='https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E7%89%A7%E6%BF%91%E7%BA%A2%E8%8E%89%E6%A0%96+%E5%A4%B4%E5%83%8F&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&word=%E7%89%A7%E6%BF%91%E7%BA%A2%E8%8E%89%E6%A0%96+%E5%A4%B4%E5%83%8F&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&expermode=&force=&pn='+str(i)+'&rn=30&gsm=&1571824887885=', headers=headers)
    res = ur.urlopen(req).read().decode()
    l = re.findall('"ObjURL":"(.*?)",', res)
    print(l)
    pic_urls.extend(l)
for p_url, n in zip(pic_urls, range(len(pic_urls))):
    try:
        ur.urlretrieve(url=baidtu_uncomplie(p_url), filename='./pic/牧濑红莉栖2/'+str(n)+'.jpg',)
    except:
        print("n''", n)
    print(p_url)


