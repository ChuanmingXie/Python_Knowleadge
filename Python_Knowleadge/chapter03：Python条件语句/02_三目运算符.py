# -*- coding:utf-8 -*-

"""
DateTime    :2021/8/4 21:14
Author      :chuanmingxie
File        :02_三目运算符.py
Software    :PyCharm
Description :
"""

sex = '男'
if sex == '男':
    ta = '他'
else:
    ta = '她'
print(ta)

ta2 = '他' if sex == '男' else '她'
print(ta2)
