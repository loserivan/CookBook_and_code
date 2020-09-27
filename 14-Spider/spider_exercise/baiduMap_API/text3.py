import pymysql
import requests
from spider_exercise.baiduMap_API.MysqlAPI import Sql

db = pymysql.connect('localhost', 'root', 'root', 'baidumap')
cursor = db.cursor()


city_list = []
with open('cities.txt', 'r', encoding='utf8') as f:
    for eachlin in f:
        # print(eachlin)
        fileds = eachlin.split('\t')
        city = fileds[0]
        city_list.append(city)

# print(city_list)
# print(len(city_list))


def getjson(loc, page_num=0):
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/85.0.4183.102 Safari/537.36'
    }
    data = {
        "query": "公园",
        "region": loc,
        "scope": "2",
        "page_size": 20,
        "page_num": page_num,
        "output": "json",
        "ak": "DTwhErf9qVVceyDez34szPbLKnTcbixK"
    }
    url = "http://api.map.baidu.com/place/v2/search?"
    rsp = requests.get(url, params=data, headers=headers)
    decodejson = rsp.json()
    # print(rsp.url)
    return decodejson


for eachcity in city_list:
    flag = True
    page_num = 0
    while flag:
        decodejson = getjson(eachcity, page_num)
        if decodejson['results']:
            for eachone in decodejson['results']:
                try:
                    park = eachone['name']
                except:
                    park = None
                try:
                    location_lat = eachone['location']['lat']
                except:
                    location_lat = None
                try:
                    location_lng = eachone['location']['lng']
                except:
                    location_lng = None
                try:
                    address = eachone['address']
                except:
                    address = None
                try:
                    street_id = eachone['street_id']
                except:
                    street_id = None
                try:
                    uid = eachone['uid']
                except:
                    uid = None

                print(eachcity, park, location_lat,
                      location_lng, address, street_id, uid)
                Sql.insert_city(
                    eachcity, park, location_lat,
                    location_lng, address, street_id, uid
                )
            page_num += 1
        else:
            flag = False
