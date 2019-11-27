# -*- coding: utf-8 -*-
import random

from day06_source_code.zhilian.zhilian.settings import UA, proxies


class ZhilianDownloaderMiddleware(object):

    def process_request(self, request, spider):
        ua = random.choice(UA)
        proxy = random.choice(proxies)
        request.headers['User-Agent'] = ua
        request.meta['proxy'] = proxy
        return None

