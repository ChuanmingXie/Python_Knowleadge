# -*- coding:utf-8 -*-

"""
DateTime    :2021/8/4 21:14
Author      :chuanmingxie
File        :judge.py
Software    :visual studio
Description :三目运算符的使用
"""

def judgebranch():
    sex = '男'
    if sex == '男':
        ta = '他'
    else:
        ta = '她'
    print(ta)

    ta2 = '他' if sex == '男' else '她'
    print(ta2)
