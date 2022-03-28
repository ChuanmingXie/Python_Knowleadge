# -*- coding:utf-8 -*-

"""
DateTime    :2021/8/1 18:12
Author      :chuanmingxie
File        :orderprint.py
Software    :visual studio
Description :顺序输出语句
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

def studyprint():
    print("选择演示算法")
    print("-------------1.数字输入测试    -------------")
    print("-------------2.用户信息输入测试-------------")
    N=int(input('请选择测试类别:'))
    if(N==1):
        printnumber()
    elif(N==2):
        printuserinfo()
