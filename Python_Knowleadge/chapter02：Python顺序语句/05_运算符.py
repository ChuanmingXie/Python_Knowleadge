# -*- coding:utf-8 -*-

"""
DateTime    :2021/8/1 19:00
Author      :chuanmingxie
File        :05_运算符.py
Software    :PyCharm
Description :
"""

print(5 + 5 > 3 - 2)
print(5 != 3)

print('hello' in 'hello world')

text = input('请输入内容：')
if "黄" in text or '赌' in text or '毒' in text:
    print('含有敏感词汇,不予显示')
    print(text.replace('黄', '*').replace('赌', '*').replace('毒', '*'))
else:
    print(text)
