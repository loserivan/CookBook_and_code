import re
from bs4 import BeautifulSoup
import requests

url = 'https://baike.baidu.com/item/Python/407313?fr=aladdin'
headers = {
            'user-agent':
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/75.0.3770.100 Safari/537.36'
        }
rsp = requests.get(url, headers=headers)
html_cont = rsp.text

soup = BeautifulSoup(html_cont, 'lxml', from_encoding='utf-8')

new_url = set()

links = soup.find_all('a', href=re.compile(r'/item/.*?">'))

for link in links:
    # 提取href属性
    new_url = link['href']
    print(link)


