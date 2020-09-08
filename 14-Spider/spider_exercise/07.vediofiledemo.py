# with open(filename, 'wb') as f:
#     f.write()
'''
1. 获取到下载文件的URL  二进制方式下载
urllib，模块提供的urlretrieve()可以进行音频文件下载，
同时支持将远程数据下载到本地

参数
url：下载文件的url地址
filename：数据存储路径+文件名
reporthook：要求回调函数，链接上服务器或者响应数据传输下载完毕时触发该函数
            显示当前下载角进度
'''
from urllib import request
import requests
import os
from lxml import etree


def Schedule(blocknum, blocksize, totalsize):
    '''
    显示下载进度
    :param blocknum:已下载的数据块
    :param blocksize:数据块大小
    :param totalsize:远程文件大小
    :return:
    '''
    per = 100.0 * blocknum * blocksize / totalsize
    if per > 100:
        per = 100
    print("当前下载进度为：{}".format(per))


headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
}

url = 'https://www.ivsky.com/tupian/ziranfengguang/'

rsp = requests.get(url=url, headers=headers)

html = etree.HTML(rsp.text)

img_urls = html.xpath('//div[@class="il_img"]//img/@src')

for img_url in img_urls:
    root_dir = 'img'
    if not os.path.exists(root_dir):
        os.mkdir(root_dir)
    filename = img_url.split('/')[-1]
    request.urlretrieve('http:' + img_url, root_dir + '/' + filename, Schedule)
