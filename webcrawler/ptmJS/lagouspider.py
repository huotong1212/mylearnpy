import time

from pymongo import MongoClient
from selenium import webdriver  #导入Selenium的webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  #导入Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

class lagouSpider(object):
    def __init__(self):
        self.start_url = 'https://www.lagou.com/'
        self.keyword = 'python'
        self.driver = webdriver.Chrome()  #指定使用的浏览器，初始化webdriver
        self.wait = WebDriverWait(self.driver, 10)
        self.mongo_url = 'mongodb://localhost:27017'
        self.mongo_db = 'webpack'
        self.count = 0
        self.collection = 'lagou'

    def run(self):
        self.client = MongoClient(self.mongo_url)
        self.db = self.client[self.mongo_db]
        self.search()
        self.send_requests()
        print(self.count)
        self.client.close()

    def search(self):
        self.driver.get(self.start_url)  # 请求网页地址
        self.driver.find_element_by_id('cboxClose').click()

        # 输入关键字查询
        time.sleep(1)
        elem = self.driver.find_element(By.XPATH, './/input[@placeholder="搜索职位、公司或地点"]')
        elem.send_keys(self.keyword)
        elem.send_keys(Keys.RETURN)

        # 点击城市，深圳
        self.switch()
        self.click_action('//div[@id="filterCollapse"]/div[1]/div[2]/li/div[2]/div/a[3]')

        # 点击，工作经验：三年以下
        self.switch()
        self.click_action('.//div[@id="filterCollapse"]/li[1]/a[3]')

    def send_requests(self):
        while True:
            self.wait.until(EC.presence_of_element_located((By.XPATH,'.//ul[@class="item_con_list"]')))
            page = self.driver.page_source
            self.parse_content(page)
            # next_btn = self.wait.until(EC.presence_of_element_located((By.XPATH,'//div[@class="pager_container"]/span[last()]')))
            next_btn = self.driver.find_element(By.XPATH,'//div[@class="pager_container"]/span[last()]')
            #  判断是否是最后一页，如果是，退出while循环
            if 'pager_next pager_next_disabled' in next_btn.get_attribute('class'):
                break
            else:
                next_btn.click()
                time.sleep(1)

    def parse_content(self,page): # 显示等待
        soup = BeautifulSoup(page, 'lxml')

        # print(soup.title)

        all_jobs = soup.find_all('li', attrs={'data-index': True})


        # print(type(all_jobs))

        for i, child in enumerate(all_jobs):
            # print(i, child.attrs)
            item = {}
            item['company'] = child['data-company']
            item['salary'] = child['data-salary']
            item['job'] = child['data-positionname']
            item['company_detail'] = child.find('div', attrs={'class':"industry"}).string.strip()
            item['desc'] = child.find('div', attrs={'class':'li_b_r'}).string
            print(item)

            table = self.db[self.collection]
            self.count += 1
            table.insert_one(item)

    def switch(self):
        # 切换到新的页面时，获取最新的driver
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def click_action(self,xpath):
        # 点击页面某个按键操作
        elem = self.driver.find_element(By.XPATH, xpath)
        elem.click()

if __name__ == "__main__":
    lagou = lagouSpider()
    lagou.run()