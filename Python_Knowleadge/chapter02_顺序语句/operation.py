# -*- coding:utf-8 -*-

"""
DateTime    :2021/8/1 19:00
Author      :chuanmingxie
File        :operation.py
Software    :visual studio
Description :操作符测试
"""

import os,re

def rootpath():
    print('-----------------1-----------------')
    abspath=os.getcwd()                 #获取当前路径
    rootpath=os.path.abspath('..')      #获取上级路径
    print(os.path.abspath(__file__))
    print(os.path.dirname(rootpath))
    print(abspath)
    print(rootpath)

def transformpath():
    print('-----------------2-----------------')
    print(repr(repr(rootpath).strip("'")).strip("'"))   # 转义路径
    print(repr(abspath).strip("'"))
    print(str(abspath))

def listpath():
    print('-----------------3-----------------')
    ret_list = re.sub(repr(repr(rootpath).strip("'")).strip("'"), '.', repr(abspath).strip("'"))  # 获取相对路径
    print('获取到的相对路径: %s' % ret_list)
 
    print('../' + ret_list)
    print('此路径是否为文件夹：%s' % os.path.isdir('../' + ret_list))

def replacestr():
    print('hello' in 'hello world')
    text = input('请输入内容：')
    if "黄" in text or '赌' in text or '毒' in text:
        print('含有敏感词汇,不予显示')
        print(text.replace('黄', '*').replace('赌', '*').replace('毒', '*'))
    else:
        print(text)

if __name__=='__main__':
    rootpath()
    #transformpath()
    #listpath()
    replacestr()

