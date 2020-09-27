
# 动态HTML

- JS(Javascript)      一般嵌入在多媒体文件中,如网页游戏

- JQuery  在源代码中包含JQuery入口
    
        <script type="text/javascript" src="http://.../jquery-1.11.1.min.js?v=34234"></script>

- Ajax

- DHTML(Dynamic HTML)   类似于Ajax


## 解决这类页面数据抓取的方法:
    
- 1.直接从js中采集内容(比较难)
- 2.利用python的第三方库直接运行js
- 3.selenium && PhantomJS

## selenium
一个web的自动化测试工具
可以指定命令自动操作
让浏览器自动加载数据,截屏,判断网站上某些动作是否发生

- 安装
    - pip install selenium==版本号
    - https://pypi.org/simple/selenium/
- 参考文档
    - https://www.selenium.dev/documentation/zh-cn/

# PhantomJS(幽灵)
- 基于Webkit 的无界面的浏览器
- 官网： "http://phantomjs.org/download.html"