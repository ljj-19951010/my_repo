import csv

import bs4
import requests
from lxml import etree


def use_xpath_get():
    """
    : 使用css选择器解析,并写入csv文件
    :return:
    """
    with open("movie3.csv", 'w', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(('title', 'ranks', 'link'))
        for page in range(10):
            resp = requests.get(
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'},
                url=f"https://movie.douban.com/top250?start={page*25}&filter=")

            if resp.status_code == 200:
                html_obj = etree.HTML(resp.text)
                div_info = html_obj.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]')
                for info in div_info:
                    title = info.xpath('div[1]/a/span[1]/text()')[0]
                    rank = info.xpath('div[2]/div/span[2]/text()')[0]
                    link = info.xpath('div[1]/a/@href')[0]
                    writer.writerow((title, rank, link))

use_xpath_get()
