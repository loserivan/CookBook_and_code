'''
破解有道词典
V1
'''

from urllib import request, parse


def youdao(key):

    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

    data = {
        "i": "boy",
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "15971340861937",
        "sign": "d7e4be3df0e65b8647ca16b34428ed3d",
        "lts": "1597134086193",
        "bv": "9ef72dd6d1b2c04a72be6b706029503a",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTIME"
    }

    # 参数data需要是bytes格式
    data = parse.urlencode(data).encode()

    headers = {
        "Accept":
        "application/json, text/javascript, */*; q=0.01",
        # "Accept-Encoding":
        # "gzip, deflate",
        "Accept-Language":
        "zh-CN,zh;q=0.9",
        "Connection":
        "keep-alive",
        "Content-Length":
        "237",
        "Content-Type":
        "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": ("OUTFOX_SEARCH_USER_ID=138989436@10.108.160.17; "
                   "JSESSIONID=aaancDHlYuQBWdjX9MCpx; "
                   "OUTFOX_SEARCH_USER_ID_NCOO=1382447435.5381677; "
                   "___rl__test__cookies=1597134086192"),
        "DNT":
        "1",
        "Host":
        "fanyi.youdao.com",
        "Origin":
        "http://fanyi.youdao.com",
        "Referer":
        "http://fanyi.youdao.com/",
        "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/84.0.4147.125 Safari/537.36"),
        "X-Requested-With":
        "XMLHttpRequest"
    }

    req = request.Request(url=url, data=data, headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode()
    print(html)


if __name__ == '__main__':
    youdao("boy")
