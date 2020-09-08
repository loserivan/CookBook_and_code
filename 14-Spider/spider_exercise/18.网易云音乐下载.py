"""
抓取网易云音乐

下载外链
"""
from tkinter import Tk, Label, Entry, Listbox, Button
import requests
from urllib import request


def music_spider():
    # 获取用户输入的URL地址
    # url = entry.get()
    url = 


# 创建窗口
root = Tk()

# 设置窗口标题
root.title("网易云音乐下载器")

# 设置窗口大小
root.geometry("800x600")

# 设置窗口位置
root.geometry

# 设置下载器标签:请输入下载的地址
lable = Label(root, text="请输入下载的地址:", font=("黑体", 20))
# 定位
lable.grid()

# 设置输入框
entry = Entry(root, font=("黑体", 20), width="30")
entry.grid(row=0, column=1)

# 设置列表框
text = Listbox(root, font=("宋体", 20), width=56, height=14)
text.grid(row=1, columnspan=2)

# 设置按钮

# 显示窗口,显示消息循环
root.mainloop()
