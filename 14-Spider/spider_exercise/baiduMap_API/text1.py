#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
注册百度地图API账号并进行开发者认证
需求:获取全国公园信息并保持至mysql数据库中
地点检索地址:
http://api.map.baidu.com/place/v2/search?query=ATM机&tag=银行&region=北京&output=json&ak=您的ak //GET请求

base_url:
http://api.map.baidu.com/place/v2/search?
param:
    query: 公园
    region: 成都市
    scope: 2
    page_size: 20
    output: json
    ak:DTwhErf9qVVceyDez34szPbLKnTcbixK
"""
import requests


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
    print(rsp.url)
    return decodejson

a = getjson('河北省')
print(a)
