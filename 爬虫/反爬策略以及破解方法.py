"""
反爬:                破解:
    封IP地址            使用代理服务器（IP代理）(可以使用高匿名代理来隐藏身份)

"""
import random
import re


import requests
"""
如何使用代理服务器 例子1
"""

resp = requests.get("代理地址")
proxy_list = []
if resp.status_code == 200:
    proxys = resp.json()['data']
    proxy_list.append(proxys)

proxy = random.choice(proxy_list)
resp = requests.get(
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'},
    url="https://movie.douban.com/top250",
    proxies={'http': f'http://{proxy}["ip"]:{proxy}["port"]'}
)
if resp.status_code == 200:
    title_list = re.findall(r'<span class="title">([^&]+?)</span>', resp.text)
    rat_list = re.findall(r'<span class="rating_num" property="v:average">(.+?)</span>', resp.text)
    for title, rat in zip(title_list, rat_list):
        print(f"{title}", rat)
