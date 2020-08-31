'''
python对json文件操作分为编码与解码
编码
    dumps    字符串
    dump     json对象  可以通过fp文件流写入文件

解码：
    load
    loads
'''
import json
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
}

r = requests.get('http://seputu.com/', headers=headers)

soup = BeautifulSoup(r.text, 'lxml')

content = []
for mulu in soup.find_all(class_="mulu"):
    h2 = mulu.find('h2')
    if h2 != None:
        h2_title = h2.string
        # print(h2_title)
        # 获取章节内容与url地址
        list = []
        for a in mulu.find(class_="box").find_all('a'):
            href = a.get('href')
            box_title = a.get('title').split(']')[1]
            # print(href, box_title)
            list.append({'href': href, 'box_title': box_title})
        content.append({'title': h2_title, 'content': list})

with open('guichuideng.json', 'a', encoding='utf-8') as fp:
    json.dump(content, fp, ensure_ascii=False, sort_keys=True, indent=4)
