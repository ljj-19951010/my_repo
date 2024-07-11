from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.implicitly_wait(10)     # 隐式等待
# KW = browser.find_element(By.CSS_SELECTOR, 'input')
# KW.send_keys('汽车')
# KW.send_keys(Keys.ENTER)
kw = browser.find_element(By.ID, 'kw')
kw.send_keys('地图')
kw.send_keys(Keys.ENTER)
sleep(20)
# imgs = browser.find_elements(By.CSS_SELECTOR, 'input')    返回的是一个列表

