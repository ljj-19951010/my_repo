"""
Ajax ----- asynchronous javascript and xml
异步请求
局部刷新

抓取动态页面，两个方案
1.直接通过提供的API动态接口获取 ：浏览器-检查-network-fetch/xhr
"""
import json
import requests


def down_save_picture(picture):
    filename = picture[picture.rfind('/')+1:]       # 以链接中的名字作为保存的文件名
    # filename = uuid.uuid1().hex       也可以通过系统生成 唯一标识符，来命名
    resp = requests.get(picture, verify=False)          # verify 有可能会有安全保存，可以加上false
    with open(f"imgs/{filename}", 'wb') as file:
        file.write(resp.content)


def get_picture_url():
    for i in range(3):
        resp = requests.get(url=f"https://image.so.com/zjl?sn={i*30}&ch=wallpaper")
        json_dict = json.loads(resp.text)
        for wallpaper in json_dict["list"]:
            wallpaper_picture = wallpaper['qhimg_url']
            down_save_picture(wallpaper_picture)


get_picture_url()
