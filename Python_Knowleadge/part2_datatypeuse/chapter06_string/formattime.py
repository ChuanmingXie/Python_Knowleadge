# -*- coding:utf-8 -*-
"""
DateTime    :2022/3/31 15:54:30
Author      :chuanming
File        :formattime
Description :
*Copyright @ chuanming 2022. All rights reserved
"""

from timeit import timeit

def occupyformattime():
    name = 'chuanmingxie'
    age = 27
    return '%s is %s .' % (name, age)

def spotformattime():
    name = 'chuanmingxie'
    age = 27
    return '{} is {}.'.format(name, age)

def f_formattime():
    name = 'chuanmingxie'
    age = 27
    return f'{name} is {age}.'

def timecompare():
    # 使用各方法的速度比较
    print(timeit(occupyformattime, number=1000000))
    print(timeit(spotformattime, number=1000000))
    print(timeit(f_formattime, number=1000000))