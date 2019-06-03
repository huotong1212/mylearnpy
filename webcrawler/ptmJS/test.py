from selenium import webdriver  #导入Selenium的webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  #导入Keys

driver = webdriver.Chrome()  #指定使用的浏览器，初始化webdriver
driver.get("https://account.geetest.com/login")  #请求网页地址

driver.find_element(By.XPATH,'.//input[@placeholder="请输入邮箱"]').send_keys('213413')
driver.find_element(By.XPATH,'.//input[@placeholder="请输入密码"]').send_keys('432432')

driver.find_element(By.CLASS_NAME,'geetest_radar_tip').click()