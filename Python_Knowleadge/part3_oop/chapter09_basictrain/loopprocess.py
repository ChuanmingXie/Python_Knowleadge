# -*- coding:utf-8 -*-
"""
DateTime    :2022/3/31 16:38:11
Author      :chuanming
File        :processcontrol
Description :流程控制语句的综合练习
*Copyright @ chuanming 2022. All rights reserved
"""

def whileappend():
    """实现数据拼接"""
    data_list = []
    while True:
        hobby = input('请输入你的爱好(Q退出)：')
        if hobby.upper() == 'Q':
            break
        data_list.append(hobby)
    result = ','.join(data_list)
    print(result)

def whileRange():
    """while+索引 数组输出"""
    message = '转轴拨弦三两声，未成曲调先有请'
    index = 0
    while index < len(message):
        print(message[index])
        index += 1

def forloop():
    """for 循环 数据输出"""

def forloopindex():
    """for 循环＋range+索引"""

def forcountdown():
    """使用for循环实现输出倒计时效果，例如：输出内容依次是：'倒计时3秒'，'倒计时2秒'，"""

def countword():
    """让用户输入一段文本，请计算文本中 "浪" 出现的次数，并输入结果"""

def countnumber():
    """获取用户两次输入的内容，并提取其中的数字，然后实现数字的相加（转换为整型再相加）"""