# -*- coding:utf-8 -*-
"""
DateTime    :2022/3/31 15:40:07
Author      :chuanming
File        :numberformat
Description :
*Copyright @ chuanming 2022. All rights reserved
"""

def occupyformat():
    print(f'{2 ** 3 + 1}')
    # 格式化
    print('%+10x' % 11)  # 输出整数11 对应的16进制字符串，会出现异常 + 号
    print('%04d' % 5)  # 输出整数 5 且左侧填充0补齐4位
    print('%6.3f' % 2.3)  # 输出浮点数2.3 且精度位3小数点后3位
    print("%-10x" % 10)  # 输出整数10 对应的16进制字符串,且左对齐补齐10位
    print("% 10x" % 10)  # 输出整数10 对应的16进制字符串,且左侧补0对齐10位

    print('{0:+10x}'.format(10))  # 输出整数11 对应的16进制字符串
    print('{0:04d}'.format(5))  # 输出整数 5 且左侧填充0补齐4位
    print('{0:6.3f}'.format(2.3))  # 输出浮点数2.3 且精度位3小数点后3位
    print('{0:10x}'.format(10))  # 输出整数10 对应的16进制字符串,

    # 进制转化
    print('%o' % 10)  # 输出整数为10的8进制数
    print('%x' % 10)  # 输出整数为10的16进制
    print('%x' % 20)  # 输出整数为20的16进制
    for num in range(0, 20, 1):
        # print(f'{num}   {bin(num)}  {oct(num)}  {hex(num)}')
        print("{0:06b}    {1:4o}   {2:4x}".format(num, num, num))

    # 浮点数输出
    print('%f' % 1.11)  # 默认保留6为小数
    print('%.1f' % 1.11)  # 取1位小数
    print('%e' % 1.11)  # 默认6位小数，可学计数法
    print('%.3e' % 1.11)  # 取三位小数,科学计数法
    print('%g' % 1111.1111)  # 默认6位有效位数
    print('%.7g' % 1111.1111)  # 取7位有效位数
    print('%.2g' % 1111.1111)  # 取2位有效数字,自动转化为科学计数法            

    # 精度与进度
    print('{0:.2f}'.format(1232132.12321))  # 精确到小数点后两位
    print('{0:b}'.format(10))  # 二进制
    print('{0:o}'.format(10))  # 十进制
    print('{0:x}'.format(10))  # 十六进制
    print('{0:,}'.format(123232244324))  # 千分位格式化

    # 3.2.进制转换
    print(f"小明今年{22}岁")
    print(f"小明今年{22:#b}岁")
    print(f"小明今年{22:#o}岁")
    print(f"小明今年{22:#x}岁")

