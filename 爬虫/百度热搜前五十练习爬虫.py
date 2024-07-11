import bs4
import pymysql
import requests
from bs4 import BeautifulSoup


def baidu_hot_data():
    """
    爬取百度热搜前五十
    :return:
    """
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='spider_db', charset='utf8mb4')
    try:
        with conn.cursor() as cursor:
            resp = requests.get(
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'},
                url='https://top.baidu.com/board?tab=realtime')
            if resp.status_code == 200:
                soup = bs4.BeautifulSoup(resp.text, 'html.parser')
                num = 1
                url_list = []
                while num <= 50:
                    div = soup.select(
                        f'#sanRoot > main > div.container.right-container_2EFJr > div > div:nth-child(2) > div:nth-child({num}) > a > img')
                    num += 1
                    # cursor.execute(
                    #     'insert into baidu_hot50(imgs_url) values (%s)', (div[0].attrs['src'])
                    # )
                    url_list.append(div[0].attrs['src'])

                parent_divs = soup.select(f'div.content_1YWBm')
                for parent_div, url in zip(parent_divs, url_list):
                    # #sanRoot > main > div.container.right-container_2EFJr > div > div:nth-child(2) > div:nth-child(1) > div.content_1YWBm > a > div.c-single-text-ellipsis
                    titles = parent_div.select_one('a > div.c-single-text-ellipsis')      # 标题
                    # #sanRoot > main > div.container.right-container_2EFJr > div > div:nth-child(2) > div:nth-child(1) > div.content_1YWBm > div.hot-desc_1m_jR.small_Uvkd3
                    contents = parent_div.select_one('div.hot-desc_1m_jR.small_Uvkd3')     # 简述

                    # #sanRoot > main > div.container.right-container_2EFJr > div > div:nth-child(2) > div:nth-child(1) > div.content_1YWBm > div.hot-desc_1m_jR.small_Uvkd3 > a
                    links = parent_div.select_one('div.hot-desc_1m_jR.small_Uvkd3 > a')     # 标题链接
                    # #sanRoot > main > div.container.right-container_2EFJr > div > div:nth-child(2) > div:nth-child(1) > a > img
                    # img_links = parent_div.select_one('a > img')
                    cursor.execute(
                        'insert into baidu_hot50(title, contents, title_url, imgs_url) values (%s, %s, %s, %s)',
                        (titles.text, contents.text if contents else "none", links.attrs['href'], url)
                    )

                conn.commit()
                print('success')
            else:
                print('errors')

    except Exception as e:
        conn.rollback()
        print(e)
    finally:
        conn.close()


baidu_hot_data()
