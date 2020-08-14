# 验证码问题

- 验证码：防止机器人或爬虫
- 分类：
    - 简单图片
    - 极验官网："www.geetest.com"
    - 12306
    - 电话
    - google验证
- 验证码破解：
    - 通用方法：
        - 下载网页和验证码
        - 手动输入验证码
    - 简单图片
        - 使用图像识别软件或者文字识别软件
        - 可以使用第三方图像验证码破解网站，"www.chaojiying.com"
    - 极验，官网"www.geetest.com
        - 破解比较麻烦
        - 可以模拟鼠标等移动
        - 一直在进化
    - 12306
    - 电话：语音识别
    - google验证

## Tesseract

- 机器视觉领域的基础软件
- OCR：OpticalChracterRecognition，光学文字识别
- Tesseract：一个OCR库，有google赞助
- 安装：
    - windows：
    - Mac：brew install tesseract
    - Linux: apt-get install tesseract-ocr
    - 安装后设置环境变量
- 安装后还需要pytesseract
    - pip install tesseract
- 读取案例 v38
