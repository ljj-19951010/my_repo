import bs4
import requests
from openpyxl.workbook import Workbook


def use_xpath_get():
    """
    : 使用css选择器解析,并写入csv文件
    :return:
    """
    workbook = Workbook()
    sheet = workbook.active         # 拿到系统已经创建的表
    sheet.title = 'top250'
    sheet.append(("title", "links", "ranks", "content"))

    for page in range(10):
        resp = requests.get(
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'},
            url=f"https://movie.douban.com/top250?start={page*25}&filter=")

        if resp.status_code == 200:
            soup = bs4.BeautifulSoup(resp.text, 'html.parser')
            info_divs = soup.select('div.info')  # 先获取父 标签
            for info_div in info_divs:  # 通过父标签 查找下一级标签
                title = info_div.select_one('span.title:nth-child(1)')  # 标题
                link = info_div.select_one('div.hd > a')  # 链接
                rat = info_div.select_one('div.bd > div > span.rating_num')  # 评分
                content = info_div.select_one('div.bd > p.quote > span')  # 主题， 因为有空值，所以需要通过父级标签获取

                t, l, r, c = title.text, link.attrs['href'], rat.text, content.text if content else "无主题"
                sheet.append([t, l, r, c])
    workbook.save('movies.xlsx')


use_xpath_get()
