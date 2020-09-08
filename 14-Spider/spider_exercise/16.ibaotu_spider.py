import requests
from lxml import etree


class IbaotuVideoSpider(object):
    def __init__(self):
        self.headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) '
            'Gecko/20100101 Firefox/30.0'
        }
        self.offset = 1

    def start(self, url):
        rsp = requests.get(url=url, headers=self.headers)
        html = rsp.text
        html = etree.HTML(html)

        video_src = html.xpath('//div[@class="video-play"]/video/@src')
        video_src = [src.split('_')[0] for src in video_src]
        # print(video_src)

        video_title = html.xpath('//span[@class="video-title"]/text()')
        # print(video_title)

        # 处理下一页
        try:
            next_page = html.xpath('//a[@class="next"]/@href')[0]
            next_page = "http:" + next_page

            print("下一页: {}".format(next_page))
            self.write_file(video_src, video_title)
            self.start(next_page)
        except Exception as e:
            print("最后一页了")

    def write_file(self, video_src, video_title):

        for src, title in zip(video_src, video_title):
            rsp = requests.get("http:" + src, headers=self.headers)
            filename = title + '.mp4'
            print("正在下载: {}".format(filename))

            with open('D:/IbaotuDownload/video/' + filename, 'wb') as f:
                f.write(rsp.content)


def main():
    spider = IbaotuVideoSpider()
    url = 'https://ibaotu.com/shipin/7-0-0-0-0-1.html'
    spider.start(url)


if __name__ == '__main__':
    main()
