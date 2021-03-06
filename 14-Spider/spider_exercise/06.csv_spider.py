import requests
import csv
from lxml import etree
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
}

r = requests.get('http://seputu.com/', headers=headers)

html = etree.HTML(r.text)

mulus = html.xpath('//*[@class="mulu"]')

rows = []
for mulu in mulus:
    h2 = mulu.xpath('./div[@class="mulu-title"]/center/h2/text()')
    # print(h2)
    if len(h2) > 0:
        h2_title = h2[0]
        a_s = mulu.xpath('./div[@class="box"]/ul/li/a')
        for a in a_s:
            href = a.xpath('./@href')[0]
            box_title = a.xpath('./@title')[0].split(']')[1]
            # print(href, box_title, type(box_title))
            date = a.xpath('./@title')[0].split(' ')
            date = ' '.join(date[:2]).lstrip('[').rstrip(']')
            # print(date)
            content = (h2_title, box_title, href, date)
            # print(content)
            rows.append(content)

head = ['title', 'box_title', 'href', 'date']
# windows系统下新文件默认GBK格式写入,
# 常见编码问题 乱码, 或报错error:'gbk' codec can't encode
# 打开文件时设置参数encoding='utf8'可解决
# 写入csv中间隔一行空行问题, 设置参数newline=''可解决
with open('guichuideng.csv', 'a', newline='', encoding='utf8') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(head)
    f_csv.writerows(rows)
