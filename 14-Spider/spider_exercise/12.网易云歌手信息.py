'''
网易云音乐歌手信息抓取
URL = https://music.163.com/#/discover/artist/cat?id=4001&initial=0

id = 4001 歌手类别
initial = 0
init = [-1, 65-90, 0]
'''
import requests
from bs4 import BeautifulSoup
from hyper.contrib import HTTP20Adapter
import csv


def get_artists(url):
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
        'Referer':
        'https://music.163.com/',
        ':authority':
        'music.163.com'
    }
    sessions = requests.session()
    sessions.mount('https://music.163.com/', HTTP20Adapter())
    rsp = sessions.get(url, headers=headers)
    soup = BeautifulSoup(rsp.text, 'lxml')

    for item in soup.find_all('a', attrs={'class': 'nm nm-icn f-thide s-fc0'}):
        artist_name = item.string.strip()
        artist_id = item['href'].replace('/artist?id=', '').strip()
        # print(artist_id, artist_name)
        try:
            writer.writerow((artist_id, artist_name))
        except Exception as e:
            print('写入失败~~~')
            print(e)


if __name__ == '__main__':
    id_list = [
        1001, 1002, 1003, 2001, 2002, 2003, 6001, 6002, 6003, 7001, 7002, 7003,
        4001, 4002, 4003
    ]
    init_list = [-1, 0]

    # 文件保存位置
    csvfile = open('music_163_artist.csv', 'a', encoding='utf-8', newline="")
    writer = csv.writer(csvfile)
    writer.writerow(('artist_id', 'artist_name'))

    for i in range(65, 91):
        init_list.append(i)
    # print(init_list)
    for m in id_list:
        for n in init_list:
            url = "https://music.163.com/#/discover/artist/cat?id={}&initial={}".format(
                m, n)
            get_artists(url)

    csvfile.close()
