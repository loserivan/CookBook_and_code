'''
构建代理集群/队列
每次访问服务器，随机抽取一个代理
抽取可以使用 random.choice

分析步骤：
1. 构建代理群
2. 每次访问，随机选取代理并执行
'''
from urllib import request, error
import random

# 1.设置代理地址
proxy_list = [
    # 列表中存放的是dict类型的元素
    {
        "http": "14.115.107.179:808"
    },
    {
        "http": "183.3.218.34:8080"
    },
    {
        "http": "113.161.68.30:80"
    },
    {
        "http": "58.246.3.178:53281"
    }
]
# 2.创建ProxyHandler
proxy_handler_list = []
# 3. 创建Opener
opener_list = []
for proxy in proxy_list:
    proxy_handler = request.ProxyHandler(proxy)
    proxy_handler_list.append(proxy_handler)

    opener = request.build_opener(proxy_handler)
    opener_list.append(opener)

url = "http://www.baidu.com"
# 现在访问url，则使用代理服务器
try:
    # 4. 安装Opener
    opener = random.choice(opener_list)
    request.install_opener(opener)

    rsp = request.urlopen(url)
    html = rsp.read().decode()
    print(html)
except error.URLError as e:
    print(e)
except Exception as e:
    print(e)
