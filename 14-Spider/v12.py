from urllib import request

if __name__ == '__main__':
    url = "https://weibo.com/login.php#_loginLayer_1596876062675"

    headers = {
        "Cookie":
        "SINAGLOBAL=2761179527884.4897.1588233477804; Ugrow-G0=1ac418838b431e81ff2d99457147068c; SUB=_2AkMocuvlf8NxqwJRmfsRymLkbIl3ygnEieKeLho-JRMxHRl-yT9jqnUftRB6A_LFCkJsDZDRi9FzRQ6h_galLNh2LOpq; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9Wh1IFL6XaWR-IMKlAeOJLlT; login_sid_t=0e630df3faeb24c3e1d2b1590bce54c1; cross_origin_proto=SSL; YF-V5-G0=8c4aa275e8793f05bfb8641c780e617b; WBStorage=42212210b087ca50|undefined; _s_tentry=passport.weibo.com; wb_view_log=1920*10801; Apache=1340047908443.1138.1596875988810; ULV=1596875988813:21:4:4:1340047908443.1138.1596875988810:1596592891806; WBtopGlobal_register_version=434eed67f50005bd"
    }

    req = request.Request(url, headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode()

    with open("rsp.html", "w") as f:
        f.write(html)
