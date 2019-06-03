import time
from selenium import webdriver  #导入Selenium的webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  #导入Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()  #指定使用的浏览器，初始化webdriver
driver.implicitly_wait(10) #隐式等待:在查找所有元素时，如果尚未被加载，则等10秒

driver.get("https://www.lagou.com/")  #请求网页地址

driver.find_element_by_id('cboxClose').click()

time.sleep(1)
elem = driver.find_element(By.XPATH,'.//input[@placeholder="搜索职位、公司或地点"]')
elem.send_keys('python')
elem.send_keys(Keys.RETURN)

time.sleep(2)
# driver = driver.current_window_handle  # 此行代码用来定位当前页面
# driver = webdriver.Chrome.current_window_handle
driver.switch_to.window(driver.window_handles[-1])

elem = driver.find_element(By.XPATH,'//div[@id="filterCollapse"]/div[1]/div[2]/li/div[2]/div/a[3]')
elem.click()

time.sleep(2)
driver.switch_to.window(driver.window_handles[-1])

elem = driver.find_element(By.XPATH,'.//div[@id="filterCollapse"]/li[1]/a[3]')
elem.click()

# wait = WebDriverWait(driver,10)
# wait.until(EC.presence_of_element_located((By.XPATH,'.//ul[@class="item_con_list"]')))
#
# contents=driver.find_element(By.XPATH,'.//ul[@class="item_con_list"]')
# print('------------',type(contents))
# print(contents)

time.sleep(2)
driver.switch_to.window(driver.window_handles[-1])
driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')


time.sleep(3)
page = driver.page_source

from bs4 import BeautifulSoup
soup = BeautifulSoup(page, 'lxml')
# print(page)

print(soup.title)
all_jobs = soup.find('ul',attrs={'class':'item_con_list','style':'display: block;'})
jobs = all_jobs.children

for i, child in enumerate(jobs):
    print(i, child)





print(1)
print(2)