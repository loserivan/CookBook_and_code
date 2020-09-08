'''
酷狗TOP500歌曲爬取
URL: 'https://www.kugou.com/yy/rank/home/1-8888.html?from=rank'
页面信息变换
        1-23    500

存储到MongoDB
'''
import requests
from bs4 import BeautifulSoup
import time
from pymongo import MongoClient

client = MongoClient()
songs = client.kugou_db.songs

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0',
    # 'Referer': 'https://music.163.com/'
}


def kugou_spider(url):
    '''获取酷狗音乐TOP500, 保存至MongoDB'''
    rsp = requests.get(url, headers=headers)
    # print(rsp.text)
    soup = BeautifulSoup(rsp.text, 'lxml')
    # 排行
    ranks = soup.select('.pc_temp_num')
    # print(ranks)
    titles = soup.select('.pc_temp_songlist > ul > li > a')
    # print(titles)
    times = soup.select('.pc_temp_time')
    # print(times)

    for rank, title, time in zip(ranks, titles, times):
        # 歌曲排名
        rank = rank.get_text().strip()
        # 歌曲名称
        song = title.get_text().split('-')[-1].strip()
        # 歌手
        singer = title.get_text().split('-')[0].strip()
        # 歌曲时长
        song_time = time.get_text().strip()
        # print(rank, song, singer, song_time)
        # print('~~~' * 20)

        data = {
            'rank': rank,
            'song': song,
            'singer': singer,
            'song_time': song_time
        }
        songs_id = songs.insert(data)
        print(songs_id)


if __name__ == '__main__':
    urls = [
        'https://www.kugou.com/yy/rank/home/{}-8888.html?from=rank'.format(
            str(i)) for i in range(1, 24)
    ]
    for url in urls:
        kugou_spider(url)
        time.sleep(1)
