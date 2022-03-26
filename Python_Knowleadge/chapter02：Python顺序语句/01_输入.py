# -*- coding:utf-8 -*-

"""
DateTime    :2021/8/1 18:12
Author      :chuanmingxie
File        :02_输出.py
Software    :PyCharm
Description :学习python的输入功能
"""

import getpass

num1 = int(input('请输入第一个数:'))
num2 = int(input('请输入第二个数:'))
print('{0}+{1}={2}'.format(num1, num2, num1 + num2))

name = input('请输入您的姓名:')
hobby = input('请输入您的爱好:')
print(name, hobby)

username = input('请输入您的用户名:')
# password = getpass.getpass('请输入您的密码:')
password = input('请输入您的密码:')
print(username, password)
