import json
import os
from concurrent.futures import ThreadPoolExecutor

import requests


def download_imgs(imgs):
    filename = imgs[imgs.rfind('/')+1:]
    resp = requests.get(imgs)
    path = 'my_imgs'
    if not os.path.exists(path):
        os.mkdir(path)
    with open(f'{path}/{filename}', 'wb') as file:
        file.write(resp.content)


def get_imgs():
    """
    通过API接口获取数据
    :return:
    """
    num = 0
    while num < 9:
        num += 1
        with ThreadPoolExecutor(max_workers=10) as poor:
            resp = requests.get(
                url=f'https://image.so.com/zjl?sn={num*30}&ch=pet',
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}
            )
            resp_datas = json.loads(resp.text)          # 要保存数据 得先转换为json数据
            for data in resp_datas['list']:
                title = data['title']
                imgs = data['qhimg_url']
                print(title)
                # poor.submit(func, *args, **kwargs)
                poor.submit(download_imgs, imgs)


if __name__ == '__main__':
    get_imgs()
