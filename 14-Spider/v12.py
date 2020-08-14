from urllib import request

if __name__ == '__main__':
    url = "http://www.renren.com/974876148/profile"

    headers = {
        "Cookie":
        ("anonymid=kdleclvl4aeyqg; depovince=GW; _r01_=1; "
         "taihe_bi_sdk_uid=405ae5437456c5d563dd9f85409f7817; "
         "_ga=GA1.2.1887593322.1596936216; "
         "_de=183C334F9C4F85CE53537152FAFEB306; ln_uact=15000584396; "
         "ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; "
         "jebecookies=73339e69-f2bc-48fe-a4fb-7f1aa7e26ed1|||||; "
         "JSESSIONID=abcJ7hPFJIG0R-XGXhBpx; "
         "taihe_bi_sdk_session=6e1d40ff0e7a217e1c87bc73f71d7c8f; "
         "ick_login=24be1e8b-cced-4546-bbf2-972fd7323e0c; "
         "p=5610ba1f5fac9d2964ce19e1a6ed76c18; first_login_flag=1; "
         "t=02a0ceb4f161d96aaad66e17b1dc39268; "
         "societyguester=02a0ceb4f161d96aaad66e17b1dc39268; "
         "id=974876148; xnsid=24e0be52; ver=7.0; loginfrom=null")
    }
    req = request.Request(url, headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode()

    with open("rsp.html", "w", encoding='utf8') as f:
        f.write(html)
