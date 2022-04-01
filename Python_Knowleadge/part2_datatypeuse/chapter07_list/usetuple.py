# -*- coding:utf-8 -*-
"""
DateTime    :2022/4/1 20:09:28
Author      :chuanming
File        :usetuple
Description :
*Copyright @ chuanming 2022. All rights reserved
"""

def tuplearry():
    tuple1=('you',456,'English',9.34)
    print(f"{tuple1}取第二个元素={tuple1[2]}")
    print(f"{tuple1}从第二个元素切片={tuple1[1:]}")
    tuple2=(3,"you and me")
    print(f"{tuple2}的长度={len(tuple2)}")
    tuple1+=tuple2
    print(f"新的tuple1={tuple1}")
