import requests


class HtmlDownloader(object):
    """Html下载器"""
    def download(self, url):
        if url is None:
            return None

        headers = {
            'user-agent':
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/75.0.3770.100 Safari/537.36'
        }
        rsp = requests.get(url, headers=headers)

        if rsp.status_code == 200:
            rsp.encoding = 'utf-8'
            return rsp.text

        return None
