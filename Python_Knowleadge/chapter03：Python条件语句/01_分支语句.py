# -*- coding:utf-8 -*-

"""
DateTime    :2021/8/4 21:11
Author      :chuanmingxie
File        :01_分支语句.py
Software    :PyCharm
Description :
"""

# 1.基本条件语句
age = 23
if age >= 18:
    print('已成年,可以上网吧')
else:
    print('你好小,学习重要')

# 2.多条件判断
day = 3
if day == 1:
    print('今天是周一')
elif day == 2:
    print('今天是周二')
else:
    print('今天不是周一和周二')

day = int(input('请输入一个数字(1-7):'))
if day == 1:
    print('星期一')
elif day == 2:
    print('星期二')
elif day == 3:
    print('星期3')
elif day == 4:
    print('星期4')
elif day == 5:
    print('星期5')
elif day == 6:
    print('星期6')
elif day == 7:
    print('星期7')
else:
    print('数字不能超过7')

# 3.条件嵌套
username = 'banden'
password = 'trump'
if username == 'banden':
    if password == 'trump':
        print('胜选')
    else:
        print('失败')
else:
    print('用户名错误')

username = '管理员1'
pwd = '666'
if username == '管理员':
    if pwd == '666':
        print('登陆成功')
    else:
        print('密码错误')
else:
    print('用户名错误')
