'''
Ajax异步加载

??????????????????????????????????????
'''
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
}

url = 'https://www.pexels.com/zh-cn/?page=1'

# print(urls)

reponse = requests.get(url, headers=headers)
html = reponse.text
print(html)
# soup = BeautifulSoup(reponse.text, 'lxml')
# imgs = soup.select('article > a > img')
# print(imgs)
