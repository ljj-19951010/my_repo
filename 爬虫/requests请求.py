import requests

resp = requests.get('https://scpic.chinaz.net/files/default/imgs/2024-07-03/50bf2367398c90a1.jpg')        # 响应对象
with open('img1.jpg', 'wb') as file:
    file.write(resp.content)
print('success')
