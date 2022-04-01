# -*- coding:utf-8 -*-
"""
DateTime    :2022/4/1 20:52:56
Author      :chuanming
File        :useset
Description :set和frozenset定义普通可变集合和不可变集合
*Copyright @ chuanming 2022. All rights reserved
"""

def setbase():
    sample1=set('understand')
    print(f"sample1={sample1}")
    mylist=[4,6,-1.1,'English',0,'python']
    sample2=set(mylist)
    print(f"sample2={sample2}")
    sample3=frozenset(mylist)
    print(f"sample3={sample3}")

def setoperation():
    mylist=[4,6,-1.1,'English',0,'Python']
    sample1=set(mylist)
    sample2=frozenset([6,'chinese',9])
    print(f"判断6是否在{sample1}={6 in sample1}")
    print(f"{sample1}>={sample2}的非绝对超集关系={sample1>=sample2}")
    print(f"{sample1}-{sample2}的差集运算={sample1-sample2}")
    print(f"{sample1}&{sample2}的交集运算={sample1 & sample2}")
    print(f"{sample1}并运算{sample2}并复制给1={sample1|sample2}")
    print(f"{sample1}")

def setinnerfun():
    """不可变集合frozenset无法使用内置函数"""
    sample1=set([4,6,-1.1,'English',0,'Python'])
    print(f"{sample1}add('China')元素{sample1.add('China')}")
    sample1.add('China')
    print(f"{sample1}")
    print(f"{sample1}update(France)元素{sample1.update('France')}")
    print(f"{sample1}")
    print(f"{sample1}remove(-1.1)元素{sample1.remove(-1.1)}")
    print(f"{sample1}")

    
