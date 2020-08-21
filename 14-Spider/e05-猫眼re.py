from urllib import request
import re
'''
利用正则来爬取猫眼电影
1. url：https://maoyan.com/board
2. 把电影信息尽可能多的拿下来

分析
1. 一个影片的内容是以dd开头的单元
2. 在单元内存在一部电影的所有信息

方法：
1. 把页面下载下来
2. 提取dd单元为单位的内容
3. 对每一个dd进行单独信息提取
'''

# 1.下载页面内容
url = "https://maoyan.com/board"

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/84.0.4147.125 Safari/537.36"
}
req = request.Request(url, headers=headers)

rsp = request.urlopen(req)
html = rsp.read().decode()

# 2.按dd提取出内容，缩小处理范围
s = r'<dd>(.*?)</dd>'
pattern = re.compile(s, re.S)
films = pattern.findall(html)
print(len(films))

# 3.从每一个dd中单独提取需要的信息
for film in films:
    # 提取电影名称
    s = r'<a.*?title="(.*?)"'
    pattern = re.compile(s)
    title = pattern.findall(film)[0]
    print(title)
