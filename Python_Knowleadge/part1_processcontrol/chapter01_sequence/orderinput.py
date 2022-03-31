# -*- coding:utf-8 -*-
"""
DateTime    :2022/3/31 16:14:53
Author      :chuanming
File        :orderinput
Description :顺序语句-输入
*Copyright @ chuanming 2022. All rights reserved
"""

def printnumber():
    """输出数字"""
    print(666)
    num1 = int(input('请输入第一个数:'))
    num2 = int(input('请输入第二个数:'))
    print('{0}+{1}={2}'.format(num1, num2, num1 + num2))    

def printuserinfo():
    """输出用户信息"""
    name = input('请输入您的姓名:')
    hobby = input('请输入您的爱好:')
    print(name, hobby)
    username = input('请输入您的用户名:')
    # password = getpass.getpass('请输入您的密码:')
    password = input('请输入您的密码:')
    print(username, password)
