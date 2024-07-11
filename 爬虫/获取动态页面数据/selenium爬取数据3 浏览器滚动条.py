import json
from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By



# 需要先安装chrome driver


"""
selenium破解反爬
"""
# options = webdriver.ChromeOptions()
# options.add_argument('--headless')      # 不显示浏览器窗口
# browser = webdriver.Chrome(options=options)
options = webdriver.ChromeOptions()
# 关闭打开浏览器时，工具栏的警告提示: 你正在使用自动化测试工具。。
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
browser = webdriver.Chrome(options=options)
# 针对webdriver
browser.execute_cdp_cmd(
    'Page.addScriptToEvaluateOnNewDocument',
    {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'}
)


browser.get('https://image.so.com/c?ch=car')
browser.implicitly_wait(10)     # 隐式等待；# 动态页面js渲染，浏览器有可能还没有加载出来，所以可以等待一会再进行下一步
# KW = browser.find_element(By.CSS_SELECTOR, 'input')    通过css选择器
# kw = browser.find_element(By.NAME, 'q')     # 通过文本框的name
# kw = browser.find_element(By.CSS_SELECTOR, 'input[name=q]')     # 选择器的属性名称
# kw.send_keys('奥迪')
# kw.send_keys(Keys.ENTER)
for _ in range(10):
    # 控制浏览器窗口
    browser.execute_script('window.scrollTo(0, document.documentElement.scrollTop + 1000);')
    sleep(2)

imgs = browser.find_elements(By.TAG_NAME, 'img')
for img in imgs:
    img_links = img.get_attribute('src')
    print(img_links)

# browser.close()
# sleep(15)

