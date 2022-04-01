# -*- coding:utf-8 -*-
"""
DateTime    :2022/4/1 17:50:55
Author      :chuanming
File        :sequence
Description :sequence类型簇
*Copyright @ chuanming 2022. All rights reserved
"""

def commsequence():
    a="Hello,I like Python Web Practice !"
    print(f"{a}截取2第位：a[1]={a[1]}")
    print(f"{a}截取到13位：a[:13]={a[:13]}")
    print(f"{a}截取7-13第位：a[7:13]={a[7:13]}")
    print(f"{a}从第15位开始截取：a[14:]={a[14:]}")
    print(f"{a}!!")
    print("ABC"*3)
    
    b=[2,4,"apple",5]
    print(f"{b}从第2位开始截取={b[1:]}")
    print(f"{a[7:13]} {b[2]}")

def arraycomm():
    a=[56,2,1,893,-0.4]
    print(f"{a}的长度={len(a)}")
    print(f"{a}的最大值={max(a)}")
    print(f"{a}的最小值={min(a)}")
    print(f"{a}被逆序后={list(reversed(a))}")
    print(f"{a}被排序后={sorted(a)}")


