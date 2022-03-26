# -*- coding:utf-8 -*-

"""
DateTime    :2021/8/1 18:45
Author      :chuanmingxie
File        :03_顺序输出.py
Software    :PyCharm
Description :
"""

# 1. 提示输出姓名，给出欢迎提示
name = input('用户名：')
print(name + '欢迎您 ！')

# 2. 提示输入姓名|位置|行为, 然后拼接显示
name = input('请输入姓名:')
position = input('请输入您所在位置:')
action = input('请说明您的行动:')
print(name + '在' + position + action)

# 3. 提示输入两个数字,计算两数之和
num1 = float(input('数字1:'))
num2 = float(input('数字2:'))
print(num1, num2, int(num1 / num2))
