# -*- coding:utf-8 -*-

"""
DateTime    :2021/8/4 9:39
Author      :chuanmingxie
File        :whileloop2.py
Software    :visual studio
Description :while循环
"""

def guessnumberbase():
    '''猜数字'''
    numReady = 66
    while True:
        numGuass = int(input('请输入数字:'))
        if numGuass == numReady:
            print('恭喜你，输入正确')
            break
        elif numGuass < numReady:
            print('你输入的数字小了')
        else:
            print('你输入的数字大了')

def printhundred():
    '''打印 1-100'''
    i = 1
    while i <= 100:
        print(i, end=',')
        i += 1
    print()

def printten():
    '''打印 10-1'''
    i = 10
    while i >= 1:
        print(i, end=',')
        i -= 1
    print()
    '''打印除7以外的 1-10'''
    i=1
    while i < 10:
        if i == 7:
            i += 1
            continue
        print(i, end=',')
        i += 1
    print()

def sumhundred():
    '''求和 1-100'''
    num = 1
    sum = 0
    while num <= 100:
        sum += num
        num += 1
    print(sum)
    print()

def oddoreven():
    '''打印 1-100 的奇偶性'''
    num=1
    while num <= 100:
        if num % 2 == 1:
            print(num, '为奇数')
        else:
            print(num, '为偶数')
        num += 1
    print()
