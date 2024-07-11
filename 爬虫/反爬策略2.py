"""
模拟登录用户
浏览器本地cookie
"""
import requests

resp = requests.get(url="https://www.baidu.com",
                    headers={"User-Agent": "Mozilla/5", "cookie": "网页cookie信息"},
                    # 或者 直接cookies={"将网页的信息自己拆分成字典形式"}
                    )
