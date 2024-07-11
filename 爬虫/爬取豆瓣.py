import re

import requests
"""
冒充浏览器
通过正则表达式获取标题
"""
resp = requests.get(
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'},
    url="https://movie.douban.com/top250")
if resp.status_code == 200:
    title_list = re.findall(r'<span class="title">([^&]+?)</span>', resp.text)
    rat_list = re.findall(r'<span class="rating_num" property="v:average">(.+?)</span>', resp.text)
    for title, rat in zip(title_list, rat_list):
        print(f"{title}", rat)
