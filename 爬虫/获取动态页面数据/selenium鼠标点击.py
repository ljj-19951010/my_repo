from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from 获取动态页面数据.selenium_tools import create_chrome_driver

browser = create_chrome_driver()
# browser.set_window_size(1920, 1080)     # 设置浏览器窗口大小
browser.get('https://image.so.com/')
browser.implicitly_wait(10)     # 设置隐式等待
# #so-search > form > div > input
kw = browser.find_element(By.CSS_SELECTOR, 'input[name="q"]')
kw.send_keys('奥迪')
# #so-search > form > button
su_button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
# 模拟鼠标点击
su_button.click()
# 显示等待，要等到搜索结果出来之后，在截图
# wait_obj = WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '这里填css选择器')))
# 模拟截屏：如果网页是动态的，截图会截个没加载出来的
browser.get_screenshot_as_file('aodi.png')
# 关闭浏览器
browser.close()
