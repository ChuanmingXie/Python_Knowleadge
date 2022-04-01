# -*- coding:utf-8 -*-
"""
DateTime    :2022/4/1 20:16:22
Author      :chuanming
File        :uselist
Description :
*Copyright @ chuanming 2022. All rights reserved
"""

def listarray():
    mylist=['you',456,'English',9.34]
    print(f"{mylist}获取第三个元素={mylist[2]}")
    mylist[2]='chinese'
    print(f"更新后的{mylist}")
    print(f"{mylist}的长度{len(mylist)}")
    numlist=[2,8,16,1,-6,53,-1]
    print(f"{numlist}排序后={sorted(numlist)}")
    print(f"{numlist}本身并不变化")
    print(f"{numlist}求和={sum(numlist)}")

def listinnerfun():
    numlist=[2,8,16,8,-6,52,-1]
    print(f"{numlist}中8的个数={numlist.count(8)}")
    print(f"{numlist}第二位插入数据9={numlist.insert(1,9)}")
    print(f"{numlist}")
