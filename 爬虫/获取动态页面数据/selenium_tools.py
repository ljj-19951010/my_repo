from selenium import webdriver


def create_chrome_driver(*, headless=False):
    """
    仅限于chrome浏览器的反反爬
    :param headless: 默认显示浏览器自动化操作
    :return: 浏览器对象
    """
    options = webdriver.ChromeOptions()
    if headless:
        # 运行自动化时，不显示浏览器
        options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    browser = webdriver.Chrome(options=options)
    # 设置浏览器webdriver项
    browser.execute_cdp_cmd(
        'Page.addScriptToEvaluateOnNewDocument',
        {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'}
    )
    return browser
