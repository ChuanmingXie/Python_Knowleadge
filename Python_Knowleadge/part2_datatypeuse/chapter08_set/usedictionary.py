# -*- coding:utf-8 -*-
"""
DateTime    :2022/4/1 21:19:45
Author      :chuanming
File        :usedictionary
Description :
*Copyright @ chuanming 2022. All rights reserved
"""
def usedictionary():
    dict1={'Language':'English','Title':'Python book','Pages':'90'}
    print(f"{dict1}的Title={dict1['Title']}")
    dict1['Date']="2022-03-31"
    print(f"{dict1}")
    dict1['Language']='Chinese'
    print(f"{dict1}")
    #相同键值出现多次只会有一个value生效
    dict2={'Language':'English','Language':'Chinese'}
    print(f"{dict2}")
