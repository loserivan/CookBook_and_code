import requests
from lxml import etree
import time
import os


def mzitu(base_url):
    '''
    爬取妹子图网站图片
    '''
    html = get_html(base_url)

    if html is not None:
        # 获取详情页信息
        img_src = html.xpath('//div[@class="postlist"]/ul/li/a/@href')
        for img_url in img_src:
            # print(img_url)
            img_parse(img_url)
    else:
        pass


def img_parse(img_url):
    '''
    处理详情页
    '''
    html = get_html(img_url)
    if html is not None:
        # 获取图片标题
        title = html.xpath('//div[@class="content"]/h2/text()')[0]
        title = title.replace(' ', '')
        # print(title)
        # 获取图片总的页数
        page_num = html.xpath('//div[@class="pagenavi"]/a/span/text()')[-2]
        # 拼接图片详情页地址
        for num in range(1, int(page_num) + 1):
            img_src = img_url + "/" + str(num)
            # print(img_src)
            download_img(img_src, title, num)
    else:
        pass


def download_img(img_src, title, num):
    '''
    下载图片
    '''
    html = get_html(img_src)
    if html is not None:
        # 获取图片具体链接地址
        img_url = html.xpath('//div[@class="main-image"]/p/a/img/@src')[0]
        # 设置下载路径
        root_dir = 'mzitu_pic'
        img_name = str(num) + '.jpg'
        root_dir = root_dir + "\\" + title

        if not os.path.exists(root_dir):
            os.makedirs(root_dir)

        headers = {
            'User-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
        }
        rsp = requests.get(img_url, headers=headers)

        with open(root_dir + "\\" + img_name, 'wb') as f:
            f.write(rsp.content)
            print(title + "~~" + img_name + '文件保存成功')
    else:
        pass


def get_html(url):
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        'Referer': 'https://www.mzitu.com/'
    }
    try:
        rsp = requests.get(url=url, headers=headers)
        time.sleep(1)
        html = etree.HTML(rsp.text)
        return html
    except Exception:
        return None


if __name__ == "__main__":
    for i in range(1, 2):
        base_url = 'https://www.mzitu.com/page/{}/'.format(str(i))
        mzitu(base_url)
