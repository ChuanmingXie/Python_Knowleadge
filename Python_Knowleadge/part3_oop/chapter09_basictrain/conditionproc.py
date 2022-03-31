# -*- coding:utf-8 -*-
"""
DateTime    :2022/3/31 16:38:59
Author      :chuanming
File        :usedatatype
Description :数据类型使用的综合练习
*Copyright @ chuanming 2022. All rights reserved
"""

import random

def condationreplace():
    """条件语句+replace"""
    # 1.将字符串中的所有的“l”替换为“p”
    name = "allow"
    result = name.replace("l", "p")
    print(result)

    # 2.将字符串中的敏感词
    print('hello' in 'hello world')
    text = input('请输入内容：')
    if "黄" in text or '赌' in text or '毒' in text:
        print('含有敏感词汇,不予显示')
        print(text.replace('黄', '*').replace('赌', '*').replace('毒', '*'))
    else:
        print(text)

def validationuser():
    """8.补充代码实现用户认证，提示用户输入手机号,验证码(不区分大小写)"""
    code = random.randrange(1000, 9999)
    code = str(code)
    msg = '欢迎登录Python APP系统，验证码为：{}，手机号：{}'.format(code, '123456')
    phone = input("请输入手机号：")
    data = input("请输入验证码：")
    if code.upper() == data.upper() and phone == '12345678':
        print('登陆成功')
    else:
        print('登录失败')
        print(msg)

def conditionjudge():
    """条件判断"""
    # 1.实现一个整数加法，用户输入的数据在加号前后有空格
    data = input("请输内容：")
    num_list = data.split("+", 1)
    v1 = int(num_list[0].strip())
    v2 = int(num_list[1].strip())
    result = v1 + v2
    print(result)

    # 1.判断用户输入的值是否以"al"开头，回复“是的”或”不是的“
    data = input("请输入内容：")
    if data.startswith("al"):
        print("是的")
    else:
        print("不是的")

    # 2.判断用户输入的值是否以”Nb“结尾,并回复”是的“或"不是的"
    data = input("请输入内容：")
    if data.endswith("Nb"):
        print("是的")
    else:
        print("不是的")

    # 3.判断用户输入的值是否为整数，如果是则转换为整形并输出，否则提示"请输入数字"
    data = input("请输入内容")
    if data.isdecimal():
        data = int(data)
        print(data)
    else:
        print("请输入数字")

    # 4.对用户输入的数据使用“+”分割,判断输入的数值是否都是数字
    data = input("请输入内容:")
    num_list = data.split("+", 1)
    if num_list[0].isdecimal() and num_list[1].isdecimal():
        print("都是整数")
    else:
        print("不全是整数")

    # 6.实现一个整数加法计算
    data = input("请输入内容：")
    num_list = data.split("+", 2)
    if num_list[0].isdecimal() and num_list[1].isdecimal():
        v1 = int(num_list[0])
        v2 = int(num_list[1])
        result = v1 + v2
        print(result)
    else:
        print("用户输入有问题")

    # 7.若需要逐个判断
    string = input("请输入内容【+号分割，如5+9】:")
    for num in string.split('+'):
        if num.isdecimal():
            print(num, '是数字类型')
        else:
            print(num, '不是数字类型')

    # 8.逐个计算数字
    string = input('请输入内容【+号分割，如5+9】')
    sumNumber = 0
    for num in string.split('+'):
        num = num.strip()
        sumNumber += int(num)
    print(string+"数字合计", '=', sumNumber)