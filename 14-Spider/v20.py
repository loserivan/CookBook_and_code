'''
爬去豆瓣电影数据
了解ajax的基本爬去方式

'''
from urllib import request
import json

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=40&limit=20"
herders = {
    'User-Agent':
    ("Mozilla/5.0 (Windows NT 6.1;WOW64) AppleWebKit/537.36 (KHTML,like GeCKO) "
     "Chrome/45.0.2454.85 Safari/537.36 115Broswer/6.0.3"),
    'Referer':
    'https://movie.douban.com/',
    'Connection':
    'keep-alive'
}
req = request.Request(url=url, headers=herders)
rsp = request.urlopen(req)
data = rsp.read().decode()

data = json.loads(data)

print(data)
