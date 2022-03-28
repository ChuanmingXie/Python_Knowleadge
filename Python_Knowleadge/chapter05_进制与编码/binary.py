# -*- coding:utf-8 -*-

"""
DateTime    :2021/8/4 21:50
Author      :chuanmingxie
File        :binary.py
Software    :PyCharm
Description :进制之间的转换
"""

def numberconvert():
    print(bin(252))  # 十进制转二进制
    print(oct(232))  # 十进制转8进制
    print(hex(218))  # 十进制转16进制

    print(int('0b10', base=2))  # 二进制转10进制
    print(int('111', base=8))  # 8进制转10进制
    print(int('522', base=16))  # 16进制转10进制

    print(oct(int('100', base=2)))  # 二进制转8进制:先从2转10再转8
    print(hex(int('100', base=2)))  # 二进制转16进制:先从2转十再转16
    print(bin(int('73', base=8)))  # 八进制转二进制：先从8转10再转2
    print(hex(int('73', base=8)))  # 8转16进制:先从8转10再转2
    print(bin(int('f31', base=16)))  # 16转二进制:先从16转10再转2
    print(oct(int('f31', base=16)))  # 16转8进制:先从16转10再转8

    '''十进制转其他进制'''
    for num in range(0, 20, 1):
        # print(f'{num}   {bin(num)}  {oct(num)}  {hex(num)}')
        print("{0:06b}    {1:4o}   {2:4x}".format(num, num, num))

    '''其他进制转十进制'''
    num = 210
    bin_num = bin(num)
    print(f'{bin_num}  {int(bin_num, base=2)}')

    oct_num = oct(num)
    print(f'{oct_num}  {int(oct_num, base=8)}')

    hex_num = hex(num)
    print(f'{hex_num}  {int(hex_num, base=16)}')
