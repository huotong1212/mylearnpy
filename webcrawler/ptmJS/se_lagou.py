import time

from selenium import webdriver  #导入Selenium的webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  #导入Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()  #指定使用的浏览器，初始化webdriver
# driver.implicitly_wait(10) #隐式等待:在查找所有元素时，如果尚未被加载，则等10秒
driver.get("https://www.lagou.com/jobs/list_python?px=default&gj=3%E5%B9%B4%E5%8F%8A%E4%BB%A5%E4%B8%8B&city=%E6%B7%B1%E5%9C%B3#filterBox")  #请求网页地址

# https://www.lagou.com/jobs/list_python?px=default&gj=3%E5%B9%B4%E5%8F%8A%E4%BB%A5%E4%B8%8B&city=%E6%B7%B1%E5%9C%B3#filterBox
wait = WebDriverWait(driver,10)
wait.until(EC.presence_of_element_located((By.XPATH,'.//ul[@class="item_con_list"]')))

contents=driver.find_element(By.XPATH,'.//ul[@class="item_con_list')
print(contents)






