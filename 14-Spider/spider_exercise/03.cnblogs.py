import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
    'accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,'
    'image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Cache-Control': 'max-age=0'
}

html = requests.get('https://www.cnblogs.com/legacy/cate/python/')
# print(html.text)

soup = BeautifulSoup(html.text, 'lxml')

items = soup.select('div[class="post_item_body"]')
# print(items)

for item in items:
    # 标题
    title = item.select('h3 a[class="titlelnk"]')[0].get_text()
    # 详情页链接
    href = item.select('h3 a[class="titlelnk"]')[0]['href']
    # 作者
    author = item.select('div a[class="lightblue"]')[0].get_text()
    # 作者主页
    author_home = item.select('div a[class="lightblue"]')[0]['href']
    # 简要
    infos = item.select('p[class="post_item_summary"]')[0].get_text().strip('\n').strip(' ').strip('\n')
    # print(infos)
    # 发布日期
    dates = item.select('div[class="post_item_foot"]')[0].get_text()
    dates = dates.split(' ')
    # print(dates, type(dates))
    time = dates[17] + " " + dates[18]
    # print(time)
    # 评论数
    comment_num = dates[-21].lstrip('评论(').split(')')[0]
    # print(comment_num)
    # 阅读数
    read_num = dates[-1].lstrip('\n阅读(').split(')')[0]
    # print(read_num)

