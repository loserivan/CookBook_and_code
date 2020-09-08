import requests
from lxml import etree
import sys
from hupu_mongo import MongoAPi
sys.path.append(r'C:\Users\Ivan\课程讲义\14-Spider\spider_exercise\hupu_mongo.py')


def hupu_spider(url):
    '''爬取虎扑论坛页面'''
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) '
        'Gecko/20100101 Firefox/30.0'
    }
    rsp = requests.get(url, headers=headers)
    html = rsp.text
    # print(html)
    html = etree.HTML(html)
    return (html)


def parse(html):
    '''解析页面内容'''
    # 标题
    titles = html.xpath(
        '//div[@class="titlelink box"]/a/text()|//div/a/b/text()')
    # print(titles)
    # print(len(titles))

    # 获取详情页链接信息
    parse_hrefs = html.xpath('//div[@class="titlelink box"]/a/@href')
    parse_hrefs = [
        'https://bbs.hupu.com' + parse_href for parse_href in parse_hrefs
    ]
    # print(parse_hrefs)

    # 获取作者
    authors = html.xpath('//div[@class="author box"]/a[1]/text()')

    # 获取发布日期
    dates = html.xpath('//div[@class="author box"]/a[2]/text()')

    # 获取回复数和浏览数
    answers = html.xpath('//li/span/text()')
    replies = [answer.split('\xa0/\xa0')[0] for answer in answers]
    views = [answer.split('\xa0/\xa0')[1] for answer in answers]
    # print(replies, views)

    # 获取最后回复时间和回复人
    endreply_dates = html.xpath('//div[@class="endreply box"]/a/text()')
    endauthors = html.xpath('//div[@class="endreply box"]/span/text()')
    # print(endreply_dates, endauthors)

    items = zip(titles, parse_hrefs, authors, dates, replies, views,
                endreply_dates, endauthors)
    return items


def data_storage(items):
    '''数据存储到MongoDB'''
    # print(items)
    hupu_post = MongoAPi('localhost', 27017, 'hupu', 'nba')

    for item in items:
        hupu_post.add({
            'titles': item[0],
            'parse_hrefs': item[1],
            'authors': item[2],
            'dates': item[3],
            'replies': item[4],
            'views': item[5],
            'endreply_dates': item[6],
            'endauthors': item[7],
        })


def main():
    urls = ['https://bbs.hupu.com/nba-{}'.format(str(i)) for i in range(1, 11)]
    n = 1
    for url in urls:
        print('正在抓取第{}页的数据'.format(str(n)))
        n += 1
        html = hupu_spider(url)
        data_storage(parse(html))


if __name__ == '__main__':
    main()
