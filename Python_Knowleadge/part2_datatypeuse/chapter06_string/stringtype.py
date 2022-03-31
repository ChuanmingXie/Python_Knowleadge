# -*- coding:utf-8 -*-
"""
DateTime    :2022/3/31 15:40:39
Author      :chuanming
File        :stringtype
Description :字符串类型定义和使用
*Copyright @ chuanming 2022. All rights reserved
"""

def stringuse():
    """定义字符串数据类型"""
    string1='人生只管努力，其他交给天意'
    string2="人生只管努力，其他交给天意"
    string3="""人生只管努力，其他交给天意"""
    string4='''人生只管努力，其他交给天意'''
    string5='人生不得已，自己当"主角"'
    string6="人生不得已，自己当'主角'"

    string7='孟子曰：爱人者，仁恒爱之；敬人者，人恒敬之'
    print(string7.startswith('孟子曰'))
    print(string7.endswith('之'))

    string8="zhangkuangying"
    print(string8)
    print(string8[0:-1])
    print(string8[0])
    print(string8[2:8])
    print(string8[2:])
    print(string8*2)
    print(sring8+'Text')

    print("""
    墙角数枝梅,
    凌寒独自开.
    遥知不是雪,
    为有暗香来.
    """)

def stringsection():
    """字符串切片的使用"""
    name = "生活不是电影,生活比电影沉重"
    print(name[8:1:-1])  # 从第9位倒序到都二位 ‘活生,影电是不’
    print(name[-1:1:-1])  # 从最后一位倒序到第二位 ’重沉影电比活生,影电是不‘
    print(name[-1::-1])  # 从最后一位倒叙到第一位 ’重沉影电比活生,影电是不活生‘
        
    # 2. 现有v1=123和v2=456.请将这两个值转化为二进制，并将0b字符去除，链接两二进制数后再次转化为十进制
    v1 = 123
    v2 = 456
    # vBin1 = bin(v1)
    # vBin2 = bin(v2)
    # data = vBin1[2:] + vBin2[2:]
    data = bin(v1)[2:] + bin(v2)[2:]
    result = int(data, base=2)
    print(result)

    # 3.对上提的二进制补齐0后再次拼接转换
    vv1 = 123
    vv2 = 456
    data2 = bin(vv1)[2:].zfill(16) + bin(vv2)[2:].zfill(16)
    print(int(data2, base=2))

    # 实现字符串反转
    name = "上官秦风"
    data = name[::-1]
    print(data)

    # 现有字符串 s='123a456c',请测试切片方法
    s = '123a456c'
    print(s[0:3])
    print(s[3:6])
    print(s[-1])
    print(s[len(s) - 1])
    print(s[-3:0:-2])

def stringfun():
    """字符串函数"""
    # 屏蔽敏感词，将文本中的’最有效‘、’立马见效‘等 替换为’***‘
    text = input('请输入内容:')
    text = text.replace('最有效', '***')
    text = text.replace('立马见效', '***')
    # 拼接字符串 
    print('君子'+'成人之美')
    print('小人常戚戚' * 3)