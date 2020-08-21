import requests
from lxml import etree
import json
'''
爬取嗅事百科
分析：
1.用requests爬取页面，etree解析页面，用XPath、re来提取信息
2.可提取信息：用户图像连接、段子内容、点赞次数、好评次数等
3.保存到json文件中

步骤：
1.下载页面
2.用xpath提取信息
3.保存文件
'''
base_url = "https://www.qiushibaike.com"
headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/84.0.4147.125 Safari/537.36"
}
# 下载页面
rsp = requests.get(base_url, headers=headers)
# 把页面转换成xpath对象
html = etree.HTML(rsp.text)
# 获取最大页面数
max_page = html.xpath('//span[@class="page-numbers"]/text()')[-1].strip()
# print(max_page)

list = []
for page in range(1, int(max_page) + 1):
    # https://www.qiushibaike.com/text/1/
    url = base_url + '/text/page/' + str(page) + '/'
    rsp = requests.get(url, headers)
    html = etree.HTML(rsp.text)
    article_list = html.xpath('//div[contains(@id, "qiushi_tag")]')

    for site in article_list:
        # print(site)
        item = {}
        # 段子作者
        author = site.xpath(
            './/div[@class="author clearfix"]/a/h2/text()')[0].strip()
        # print(author)
        # 段子内容
        content = site.xpath('.//div[@class="content"]/span[1]/text()')
        content = '<br/>'.join(content).strip()
        # print(content)
        # 笑脸数
        stats_vote = site.xpath('.//div[@class="stats"]/span[1]/i/text()')[0]
        # 评论数
        stats_comments = site.xpath(
            './/div[@class="stats"]/span[last()]/a/i/text()')[0]
        # 段子全文链接
        content_url = site.xpath('.//div[@class="stats"]/span/a/@href')[0]
        content_url = base_url + content_url

        item['author'] = author
        item['content'] = content
        item['stats_vote'] = stats_vote
        item['stats_comments'] = stats_comments
        item['content_url'] = content_url
        list.append(item)
        # print(item)
# 保存到json文件
json.dump(list,
          open('qiushi.json', 'w', encoding='utf-8'),
          ensure_ascii=False,
          sort_keys=True,
          indent=4)
