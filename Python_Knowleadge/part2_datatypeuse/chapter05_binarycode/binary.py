# -*- coding:utf-8 -*-

"""
DateTime    :2021/8/4 21:50
Author      :chuanmingxie
File        :binary.py
Software    :PyCharm
Description :进制之间的转换
"""

def binaryconvert():
    print(bin(252))  # 十进制转二进制
    print(oct(232))  # 十进制转8进制
    print(hex(218))  # 十进制转16进制

    # 1.代码实现进制转换
    v1 = 675  # 转化为2进制
    print(bin(v1))
    v2 = "0b11000101"  # 转化为十进制
    print(int(v2, base=2))
    v3 = "11000101"  # 转化为十进制
    print(int(v3, base=2))

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

    # 字符串转整型
    # 把字符串看成十进制的值，然后再转换为 十进制整数，结果：v1 = 186
    v1 = int("186", base=10)
    # 把字符串看成二进制的值，然后再转换为 十进制整数，结果：v1 = 9 (0b表示二进制)
    v2 = int("0b1001", base=2)
    # 把字符串看成八进制的值，然后转换为 十进制整数，结果：v1 = 100 (0o表示八进制)
    v3 = int("0o144", base=8)
    # 把字符串看成十六进制的值，然后转换为 十进制整数，结果：v1 = 89 （0x表示十六进制）
    v4 = int("0x59", base=16)