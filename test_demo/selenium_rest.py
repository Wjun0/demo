import time
import random

from selenium import webdriver

from selenium.webdriver.chrome.options import Options


chrome_options = Options()
# chrome_options.add_argument('--headless')
# 创建chrome参数对象
opt = Options()
# 把chrome设置成无界面模式，不论windows还是linux都可以，自动适配对应参数
opt.add_argument('--headless')
opt.add_argument('--disable-gpu')
opt.add_argument("window-size=1024,768")
# 添加沙盒模式
opt.add_argument("--no-sandbox")
opt.add_experimental_option('excludeSwitches',['enable-automation'])

# driver = webdriver.Chrome(chrome_options=chrome_options,executable_path = 'D:\APPS\dir\chromedriver.exe')

class Weixin(object):
    def __init__(self,weixinid):
        self.driver = webdriver.Chrome(options=opt,executable_path='C:\\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe')
        self._url = "http://weixin.sogou.com"
        self.weixinid = weixinid

        test = '//*[@id="query"]'
    def run(self):
        try:
            self.driver.get(self._url)
            # print(self.driver.page_source)
            time.sleep((random.randint(1,3)))
            self.driver.find_element_by_xpath('//*[@id="query"]').send_keys(self.weixinid)
            time.sleep((random.randint(1,3)))
            self.driver.find_element_by_xpath('//*[@id="searchForm"]/div/input[4]').click()
            time.sleep(random.randint(2,5))
            # print(self.driver.window_handles)
            self.driver.find_element_by_xpath('//*[@id="sogou_vr_11002301_box_0"]/dl[3]/dd/a').click()


            handlers = self.driver.window_handles
            print(handlers)
            # print(self.driver.page_source)
            self.driver.switch_to_window(handlers[-1])
            # 切换窗口,最后一个
            # for handler in self.driver.window_handles:
            #     print(handler)
            #     self.driver.switch_to_window(handler)
            time.sleep(5)
            print(self.driver.page_source)
            print(self.driver.find_element_by_xpath('//*[@id="js_content"]'))


            data = self.driver.find_element_by_xpath('//*[@id="js_content"]').text
            print(data)


        except Exception as e:
            print(e)

        finally:
            self.driver.close()

if __name__ == '__main__':
    while True:
        # 阻塞式等待重redis 取出需要下载的微信号id
        # resp_data = r.brpop(settings.CRAWLER_CONFIG["downloader"])
        # data = json.loads(resp_data[1])
        data = {'wechatid': 'shanghaicdc', 'kind': 0, 'wechat_id': 4}
        weixin_id = data['wechatid']
        weixin_id = 'shbendibao'
        Weixin(weixin_id).run()