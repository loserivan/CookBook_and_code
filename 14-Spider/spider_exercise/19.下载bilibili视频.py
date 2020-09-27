"""
json文件:
https://api.bilibili.com/x/web-interface/search/type?page=1&keyword=%E6%90%9E%E7%AC%91&search_type=video
视频播放地址(srcurl):
http://www.bilibili.com/video/av753405579
"""
import requests
import json
import os


def getInfo(keyword, page_num):
    """获取srcurl和title"""
    data = []
    for page in range(1, page_num + 1):
        url = 'https://api.bilibili.com/x/web-interface/search/type?page={}&keyword={}&search_type=video'.format(str(page), keyword)
        html = requests.get(url).text
        html = json.loads(html)
        # print(html)
        items = html['data']['result']
        for item in items:
            # print(item)
            title = item['title']
            video_url = item['arcurl']
            # print(title, video_url)
            data.append((title, video_url))
    return data


def downloadvideo(data):
    """下载视频"""
    path = 'D:/IbaotuDownload/bilibili'
    if not os.path.exists(path):
        os.makedirs(path)

    for title, url in data:
        # 视频存放路径
        root = path + '/' + title

        print('===' * 30)
        print('正在下载: {}...'.format(title))
        # 利用os.system操作you-get进行视频下载
        os.system('you-get -o {} {}'.format(root, url))
        print('{}下载完成...'.format(title))


if __name__ == '__main__':
    data = getInfo('搞笑', 2)
    downloadvideo(data)

