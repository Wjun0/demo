import os

import requests
from lxml import etree


class Weixin_sogo():
    def __init__(self):
        self.session = requests.session()
        self.url = "https://weixin.sogou.com/"
        self.head = {
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'sec-fetch-site': 'cross-site',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Origin': 'http://www.zhi-niao.com',
        'Connection': 'keep-alive',
        # 'Cookie' : '',
    }

    def run(self):
        url = 'https://weixin.sogou.com/weixin?type=1&query=shbendibao&ie=utf8&s_from=input&_sug_=y&_sug_type_='
        res = self.session.get(url,headers=self.head)
        print(res.text)
        html = etree.HTML(res.text)
        obj_url = html.xpath('//*[@id="sogou_vr_11002301_box_0"]/dl[3]/dd/a/@href')[0]
        print(obj_url)
        base_url = 'https://weixin.sogou.com'
        url = base_url + obj_url
        print(url)

        resp = self.session.get(url,headers=self.head)
        print(resp.text)








if __name__ == '__main__':
    Weixin_sogo().run()
