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
    # print(rsp.url)
    return decodejson


province_list = [
    '河北省',
    '山西省', '辽宁省', '吉林省', '黑龙江省', '江苏省', '浙江省',
    '安徽省', '福建省', '江西省', '山东省', '河南省', '湖北省', '湖南省',
    '广东省', '海南省', '四川省', '贵州省', '云南省', '陕西省', '甘肃省',
    '青海省', '台湾省', '内蒙古自治区', '广西壮族自治区', '西藏自治区',
    '宁夏回族自治区', '新疆维吾尔自治区'
    # '北京市', '天津市', '上海市', '重庆市',
    # '香港特别行政区', '澳门特别行政区'
]
for eachprovience in province_list:
    decodjson = getjson(eachprovience)
    for eachcity in decodjson['results']:
        print(eachcity)
        city = eachcity['name']
        num = eachcity['num']
        output = '\t'.join([city, str(num)]) + '\n'
        with open('cities.txt', 'a', encoding='utf-8') as f:
            f.write(output)

special_city = [
    '北京市', '天津市', '上海市', '重庆市','香港特别行政区', '澳门特别行政区'
]

for city in special_city:
    decodjson = getjson(city)
    num = decodjson['total']
    output = '\t'.join([city, str(num)]) + '\n'
    with open('cities.txt', 'a', encoding='utf-8') as f:
        f.write(output)
