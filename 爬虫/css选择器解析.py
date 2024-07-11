import bs4
import requests


def use_css_selector():
    """
    : 使用css选择器解析
    :return:
    """
    resp = requests.get(
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'},
        url="https://movie.douban.com/top250")
    if resp.status_code == 200:
        soup = bs4.BeautifulSoup(resp.text, 'html.parser')
        # soup.select()
        # soup.select_one()       # 只拿第一个选择器
        # title = soup.select_one('span.title')
        title = soup.select('span.title:nth-child(1)')
        links = soup.select('div.hd > a')
        for t, l in zip(title, links):
            print(t.text, l.attrs['href'])
            print("/.=."*30)


use_css_selector()
