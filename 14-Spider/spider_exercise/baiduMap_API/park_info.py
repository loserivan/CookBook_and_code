"""
URL:
http://api.map.baidu.com/place/v2/detail?uid=435d7aea036e54355abbbcc8&output=json&scope=2&ak=您的密钥 //GET请求

"""
import requests
from spider_exercise.baiduMap_API.MysqlAPI import Sql


def getjson(uid):
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/85.0.4183.102 Safari/537.36'
    }
    data = {
        "uid": uid,
        "scope": "2",
        "output": "json",
        "ak": "DTwhErf9qVVceyDez34szPbLKnTcbixK"
    }
    url = "http://api.map.baidu.com/place/v2/detail?"
    rsp = requests.get(url, params=data, headers=headers)
    decodejson = rsp.json()
    # print(rsp.url)
    return decodejson


# 从数据库中获取uid号
results = Sql.read_city()
# print(results[0][0])
# print(type(results[0]))
for item in results:
    uid = item[0]
    decodejson = getjson(uid)
    # print(decodejson)
    infos = decodejson['result']
    # 获取想要的信息
    try:
        # uid
        uid = infos['uid']
    except:
        uid = None
    try:
        # street_id
        street_id = infos['street_id']
    except:
        street_id = None
    try:
        # name
        name = infos['name']
    except:
        name = None
    try:
        # address
        address = infos['address']
    except:
        address = None
    try:
        # shop_hour
        shop_hours = infos['detail_info']['shop_hours']
    except:
        shop_hours = None
    try:
        # detail_url
        detail_url = infos['detail_info']['detail_url']
    except:
        detail_url = None
    try:
        # content_tag
        content_tag = infos['detail_info']['content_tag']
    except:
        content_tag = None

    print(uid, street_id, name, address, shop_hours, detail_url, content_tag)
    Sql.insert_parkinfo(uid, street_id, name, address, shop_hours,
                        detail_url, content_tag)
