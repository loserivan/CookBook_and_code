"""
喜马拉雅音乐下载
pip install pypinyin  将中文解析成对应的拼音
"""
import requests
from urllib import request
from pypinyin import lazy_pinyin
from lxml import etree
import json
import hashlib
import time
import random
import os


class Ximalaya:
    """
    爬取喜马拉雅音乐
    :param: category 音乐分类
    """

    def __init__(self, category):
        self.base_url = 'https://www.ximalaya.com/'
        self.headers = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) '
                'Gecko/20100101 Firefox/30.0',
        }
        self.category = category
        # 添加xm-sign到headers中
        self.getSign(self.getServerTime())

    def getServerTime(self):
        """
        获取喜马拉雅服务器的时间戳
        """
        # 这个地址就是返回服务器时间戳的接口
        serverTimeUrl = self.base_url + 'revision/time'
        serverTime = self.get_html(url=serverTimeUrl)
        return serverTime

    def getSign(self, serverTime):
        """
        生成 xm-sign
        规则是 md5(himalaya-服务器时间戳)(100以内随机数)服务器时间戳(100以内随机数)现在时间戳
        """
        nowTime = str(round(time.time() * 1000))

        sign = str(
            hashlib.md5("himalaya-{}".format(serverTime).encode()).hexdigest()
        ) + "({})".format(str(round(
            random.random() * 100))) + serverTime + "({})".format(
            str(round(random.random() * 100))) + nowTime
        # 将xm-sign添加到请求头中
        self.headers["xm-sign"] = sign
        # return sign

    def get_category_list(self):
        """
        获取分类清单
        """
        url = self.base_url + 'yinyue/'
        html = etree.HTML(self.get_html(url))
        categories = html.xpath('//a[@data-code]/text()')

        print('音乐分类列表:')
        for category in categories:
            print(category)

    def get_album_info(self):
        """
        获取专辑信息:
        1. 专辑列表
        2. 专辑Id
        """
        max_page = self.get_max_page(self.category_page())
        album_titles = []
        albumIds = []
        for page_num in range(1, max_page + 1):
            url = self.base_url + 'revision/category/queryCategoryPageAlbums?category=yinyue&subcategory=' + self.fanyi(
            ) + '&meta=&sort=0&page=' + str(page_num) + '&perPage=30'
            album_info = json.loads(self.get_html(url))
            albums = album_info['data']['albums']
            for album in albums:
                album_title = album['title']
                albumId = album['albumId']
                album_titles.append(album_title)
                albumIds.append(albumId)

        return album_titles, albumIds

    def get_album_title(self):
        """
        获取对应分类的专辑标题目录
        """
        album_titles = self.get_album_info()[0]
        for album_title in album_titles:
            print(album_title)

    def get_albumId(self, album_title):
        """
        获取相应专辑标题的专辑Id
        """
        info = self.get_album_info()
        album_titles = info[0]
        albumIds = info[1]
        albumId = albumIds[album_titles.index(album_title)]
        return albumId

    def parse_info(self, album_title):
        """
        处理下载需要的信息, 获取下载专辑的音乐名称, 音乐下载
        """
        # 获取专辑页面最大页面数
        max_page = self.get_max_page(self.album_page(album_title))

        for page_num in range(1, max_page + 1):
            album_url = self.base_url + 'revision/album/v1/getTracksList?albumId=' + str(
                self.get_albumId(album_title)) + '&pageNum=' + str(page_num)

            album_json = json.loads(self.get_html(url=album_url))
            tracks = album_json['data']['tracks']

            for track in tracks:
                muisc_name = track['title']
                trackId = track['trackId']
                music_url = self.base_url + 'revision/play/v1/audio?id=' + str(
                    trackId) + '&ptype=1'

                try:
                    music_json = json.loads(self.get_html(url=music_url))
                    download_url = music_json['data']['src']
                except Exception:
                    print('获取下载URL失败!')

                self.download_album(album_title, muisc_name, download_url)

    def download_album(self, album_title, muisc_name, download_url):
        """
        下载专辑全部歌曲
        """
        print('正在下载"{}"......'.format(muisc_name))
        # rsp = requests
        print('URL: {}'.format(download_url))
        # 创建专辑文件夹
        dir = 'D:/Ximalayadownload/music/' + album_title
        if os.path.exists(dir):
            pass
        else:
            os.mkdir(dir)
        try:
            request.urlretrieve(download_url, dir + '/' + muisc_name)
            print('下载完成!')
        except Exception:
            print('下载失败......')

    def fanyi(self):
        """
        翻译要查找的歌曲类型(转换成拼音)
        """
        var = lazy_pinyin(self.category)
        str = ''.join(var)
        return str

    def category_page(self):
        """
        获取分类页面信息
        """
        url = self.base_url + 'yinyue/' + self.fanyi() + '/'
        html = etree.HTML(self.get_html(url))
        return html

    def album_page(self, album_title):
        """
        获取专辑页面信息
        """
        url = self.base_url + self.fanyi() + '/' + str(
            self.get_albumId(album_title)) + '/'
        html = etree.HTML(self.get_html(url))
        return html

    def get_html(self, url):
        """
        请求html页面
        """
        response = requests.get(url=url, headers=self.headers)
        html = response.text
        return html

    def get_max_page(self, html):
        """
        获取网页最大页数
        """
        try:
            max_page = int(html.xpath('//form/input/@max')[0])
        except Exception:
            max_page = 1
        return max_page


def main():
    while True:
        music_category = input('输入音乐类别(q): ')

        if music_category == 'q':
            break

        x = Ximalaya(music_category)
        x.get_album_info
        print('---' * 20)
        print('专辑目录: ')
        x.get_album_title()
        print('---' * 20)

        album_title = input('输入专辑标题进行下载(q): ')

        if album_title == 'q':
            break
        try:
            x.parse_info(album_title)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
