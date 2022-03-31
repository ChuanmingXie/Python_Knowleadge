# -*- coding:utf-8 -*-
"""
DateTime    :2022/3/31 16:26:12
Author      :chuanming
File        :getpath
Description :
*Copyright @ chuanming 2022. All rights reserved
"""

import sys,os

def rootpath():
    """路径系统"""
    print('-----------------1-----------------')
    abspath=os.getcwd()                 #获取当前路径
    rootpath=os.path.abspath('..')      #获取上级路径
    print(os.path.abspath(__file__))
    print(os.path.dirname(rootpath))
    print(abspath)
    print(rootpath)

def convertpath():
    """转义文件路径"""
    print('-----------------2-----------------')
    print(repr(repr(rootpath).strip("'")).strip("'"))   # 转义路径
    print(repr(abspath).strip("'"))
    print(str(abspath))

def listpath():
    """路径列表"""
    print('-----------------3-----------------')
    ret_list = re.sub(repr(repr(rootpath).strip("'")).strip("'"), '.', repr(abspath).strip("'"))  # 获取相对路径
    print('获取到的相对路径: %s' % ret_list)
 
    print('../' + ret_list)
    print('此路径是否为文件夹：%s' % os.path.isdir('../' + ret_list))


rootpath()
#convertpath()
#listpath()