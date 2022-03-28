# -*- coding:utf-8 -*-

"""
DateTime    :2021/8/4 21:53
Author      :chuanmingxie
File        :01_整形.py
Software    :PyCharm
Description :
"""

import math

'''1. 整型数据类型'''

# 整型定义
number = 10
age = 99

# 整形方法
v1 = 5
print(bin(v1))
result = v1.bit_length()
print(result)

# 查看二进制有多少个位组成
v2 = 10
print(bin(10))
result2 = v2.bit_length()
print(result2)

# 查看共轭复数
v3 = complex(2, 4)
v4 = 3 - 5j
print(v3, v4)
print(v3.real, v3.imag)
print(v3.conjugate(), v4.conjugate(), v3.conjugate()+v4.conjugate())

# 整数运算
print(1 + 2)        # 1. 加
print(3 - 1)        # 2. 减
print(10 * 3)       # 3. 乘
print(10 / 3)       # 4. 除
print(10 // 3)      # 5. 求商/取整
print(10 % 3)       # 6. 取余/模
print(2 ** 10)      # 7. 幂

# 布尔值转整型
n1 = int(True)      # True转换为整数 1
n2 = int(False)     # False转换为整数 0
# 字符串转整型
v1 = int("186", base=10)     # 把字符串看成十进制的值，然后再转换为 十进制整数，结果：v1 = 186
v2 = int("0b1001", base=2)   # 把字符串看成二进制的值，然后再转换为 十进制整数，结果：v1 = 9 (0b表示二进制)
v3 = int("0o144", base=8)    # 把字符串看成八进制的值，然后转换为 十进制整数，结果：v1 = 100 (0o表示八进制)
v4 = int("0x59", base=16)    # 把字符串看成十六进制的值，然后转换为 十进制整数，结果：v1 = 89 （0x表示十六进制）
# 浮点型（小数）
print(int(8.7))   # 8

'''浮点数数据类型'''
v1 = 3.14
v2 = 9.89

# 1. 浮点数转换为int型时,会将小数部分去掉
print(int(3.14))
# 2.使用round函数保留N位有效小数
print(round(3.1415926, 4))
# 3.浮点数精度上的计算问题
v1 = 0.1
v2 = 0.2
v3 = v1 + v2
print(v3)
# 4.使用decimal解决精度问题
import decimal
v1 = decimal.Decimal('0.1')
v2 = decimal.Decimal('0.2')
print(v1 + v2)

