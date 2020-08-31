from urllib import request, parse
import time
import random
import json
'''
破解有道词典
V2
处理js加密代码
'''
'''
通过查找，能找到js代码中操作代码
1. 这个是计算salt的公式
i = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10));
2. sign: n.md5("fanyideskweb" + t + i + "]BjuETDhU)zqSxf-=B#7m");
md5一共需要四个参数，第一个和第四个都是固定值的字符串，第三个是所谓的salt，第二个是
第二个参数就是输入的要查找的单词

'''

r = int(time.time() * 1000)
ua = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
      "AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/84.0.4147.125 Safari/537.36")


def getSalt():
    '''
    salt公式是:
    r = "" + ((new Date).getTime()
    salt = r + parseInt(10 * Math.random(), 10));
    把他翻译成python代码
    :return:
    '''
    salt = r + random.randint(0, 10)

    return salt


def getMD5(v):
    import hashlib
    md5 = hashlib.md5()

    # update需要一共bytes格式的参数
    md5.update(v.encode("utf-8"))
    sign = md5.hexdigest()

    return sign


def getSign(key, salt):

    sign = "fanyideskweb" + key + str(salt) + "]BjuETDhU)zqSxf-=B#7m"
    sign = getMD5(sign)

    return sign


def getBv():

    bv = getMD5(ua)

    return bv


def fanyi_parse(html):
    data_json = json.loads(html)
    try:
        items = data_json['smartResult']['entries']
        for item in items:
            print(item)
    except Exception:
        print('请输入正确的单词!')


def youdao(key):

    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

    salt = getSalt()

    data = {
        "i": key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": str(salt),
        "sign": getSign(key, salt),
        "lts": str(r),
        "bv": getBv(),
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTIME",
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
        len(data),
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
        "User-Agent":
        ua,
        "X-Requested-With":
        "XMLHttpRequest"
    }

    req = request.Request(url=url, data=data, headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode()
    fanyi_parse(html)


if __name__ == '__main__':
    while True:
        key = input('请输入单词(q退出)：')
        if key == 'q':
            break
        youdao(key)
