from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import time
import pandas as pd
import os

# headless模式(无界面)
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920x1080')  # 设置窗口大小
# 启动浏览器
browser = webdriver.Chrome(chrome_options=options)
wait = WebDriverWait(browser, 10)


def index_page(page):
    try:
        print('正在抓取第{}页'.format(page))
        # 等待加载完表格
        wait.until(ec.presence_of_all_elements_located((By.ID, 'dt_1')))
        if page > 1:
            # 找到页数输入框
            input = wait.until(
                ec.presence_of_element_located(
                    (By.XPATH, '//*[@id="PageContgopage"]')
                )
            )
            input.click()
            input.clear()
            input.send_keys(page)
            submit = wait.until(
                ec.element_to_be_clickable(
                    (By.CSS_SELECTOR, '#PageCont > a.btn_link')
                )
            )
            submit.click()
            time.sleep(2)
        # 确认是否成功跳转页面
        wait.until(
            ec.text_to_be_present_in_element(
                (By.CSS_SELECTOR, '#PageCont > span.at'), str(page)
            )
        )
    except Exception:
        return None


def parse_table():
    """提取表格内容"""
    # element = wait.until(ec.presence_of_all_elements_located((By.ID, 'dt_1')))
    # 或者
    element = browser.find_element_by_css_selector('#dt_1')
    # 提取表格内容
    td_content = element.find_elements_by_tag_name('td')

    lst = []
    for td in td_content:
        lst.append(td.text)

    # 确定表格列数
    col = len(element.find_elements_by_css_selector('tr:nth-child(1) td'))
    # 表格内容按行分组处理
    lst = [lst[i : i + col] for i in range(0, len(lst), col)]
    # 获取详情页面链接
    lst_link = []
    links = element.find_elements_by_css_selector('#dt_1 a.red')
    for link in links:
        url = 'http://data.eastmoney.com' + link.get_attribute('href')
        lst_link.append(url)
    lst_link = pd.Series(lst_link)
    df_table = pd.DataFrame(lst)
    df_table['url'] = lst_link

    return df_table


def save(df_table, report):
    """存储获取的表格信息"""
    fill_path = r'C:\Users\Ivan\课程讲义\14-Spider\spider_exercise\DHTML\东方财富网'
    if not os.path.exists(fill_path):
        os.makedirs(fill_path)
    os.chdir(fill_path)
    df_table.to_csv('{}.csv'.format(report), mode='a', header=False)


def set_table():
    print('***' * 30)
    print('\t\t\t\t东方财富网年季报下载')
    print('...' * 30)
    # 设置要查询的财务报表年份
    year = int(float(input('请输入要查询的年份(如2020): \n')))
    # 设置季度
    quarter = int(float(input('请输入季度(1-4): ')))
    while quarter > 4 or quarter < 1:
        quarter = int(float(input('请重新输入季度(1-4): ')))
    quarter = '{:02d}'.format(quarter * 3)
    dict_quarter = {
        '03': '一季报',
        '06': '中报',
        '09': '三季报',
        '12': '年报'
    }
    # 日期
    date = '{}{}'.format(year, quarter)
    # 设置报表类型
    type = int(
        input(
            '请输入查询报表对应数字(1-业绩报表, 2-业绩快报, 3-业绩预告, 4-预约披露时间,'
            '5-资产负债表, 6-利润表, 7-现金流量表): '
        )
    )
    dict_type = {
        1: '业绩报表',
        2: '业绩快报',
        3: '业绩预告',
        4: '预约披露时间',
        5: '资产负债表',
        6: '利润表',
        7: '现金流量表'
    }
    dict = {
        1: 'yjbb',
        2: 'yjkb',
        3: 'yjyg',
        4: 'yysj',
        5: 'zcfz',
        6: 'lrb',
        7: 'xjll'
    }
    report = str(year) + '年' + dict_quarter[quarter] + dict_type[type]
    category = dict[type]
    # 设置url地址
    url = 'http://data.eastmoney.com/bbsj/{}/{}.html'.format(date, category)
    # 设置爬取的页数
    start_page = int(input('请输入下载起始页: '))
    nums = input('请输入要下载多少页: ')

    print('***' * 30)

    # 确定页面最后一页
    browser.get(url)
    page = browser.find_element_by_css_selector(
        '#PageCont > a:nth-last-child(5)')
    max_page = int(page.text)

    while start_page > max_page:
        start_page = int(input('超过最大页,请重新输入下载起始页: '))

    if nums.isdigit():
        end_page = start_page + int(nums)
        if end_page > max_page + 1:
            end_page = max_page + 1
    else:
        print('页数有误')

    print('准备下载:{}'.format(report))
    print(url)
    yield {
        'url': url,
        'report': report,
        'start_page': start_page,
        'end_page': end_page
    }


def main(report, page):
    try:
        index_page(page)
        df_table = parse_table()
        save(df_table, report)
        print('第{}页抓取完成'.format(page))
        print('...' * 30)
    except Exception as e:
        print(e)
        print('抓取失败')


if __name__ == '__main__':
    while True:
        for i in set_table():
            report = i.get('report')
            start_page = i.get('start_page')
            end_page = i.get('end_page')

            for page in range(start_page, end_page):
                main(report, page)

            print('全部抓取完成')

        i = input('继续/退出(q): ')
        if i == 'q':
            break
        else:
            continue
