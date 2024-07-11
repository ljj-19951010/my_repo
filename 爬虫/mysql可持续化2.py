import bs4
import pymysql
import requests


conn = pymysql.connect(host='localhost', user='root', password='root', database='spider_db', charset='utf8mb4', port=3306)
try:
    with conn.cursor() as cursor:
        for page in range(10):
            resp = requests.get(
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'},
                url=f"https://movie.douban.com/top250?start={page * 25}&filter=")

            if resp.status_code == 200:
                soup = bs4.BeautifulSoup(resp.text, 'html.parser')
                movies_list = []
                info_divs = soup.select('div.info')  # 先获取父 标签
                for info_div in info_divs:  # 通过父标签 查找下一级标签
                    title = info_div.select_one('span.title:nth-child(1)')  # 标题
                    link = info_div.select_one('div.hd > a')  # 链接
                    rat = info_div.select_one('div.bd > div > span.rating_num')  # 评分
                    content = info_div.select_one('div.bd > p.quote > span')  # 主题， 因为有空值，所以需要通过父级标签获取
                    movies_list.append((title.text, link.attrs['href'], rat.text, content.text if content else None))

                # 批处理，直接全部插入到数据表里
                cursor.executemany(
                        'insert into top_movie(title, url, rating, subject) values (%s, %s, %s, %s)', movies_list
                    )
    conn.commit()

except Exception as e:
    conn.rollback()
    print(e)

finally:
    conn.close()
