# -*- coding:utf-8 -*-
"""
DateTime    :2022/3/31 17:11:21
Author      :chuanming
File        :processcontrol
Description :
*Copyright @ chuanming 2022. All rights reserved
"""

import sys,os
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir+"\\part1_processcontrol\\chapter01_sequence")
sys.path.append(base_dir+"\\part1_processcontrol\\chapter02_selection")

import orderinput,orderprint,branch,condition,judge


def studyprint():
    print("选择演示算法")
    print("-------------1.输入数字测试-------------")
    print("-------------2.输入用户测试-------------")
    print("****************************************")
    print("-------------3.打印佛祖测试-------------")
    print("-------------4.打印小诗测试-------------")
    print("-------------5.打印用户测试-------------")
    print("****************************************")    
    print("-------------6.基本条件语句-------------")
    print("-------------7.多分支断语句-------------")
    print("-------------8.条件嵌套语句-------------")

    N=int(input('请选择测试类别:'))
    if(N==1):
        orderinput.printnumber()
    elif(N==2):
        orderinput.printuserinfo()
    elif(N==3):
        orderprint.buddhistimg()
    elif(N==4):
        orderprint.printverse()
    elif(N==5):
        orderprint.userinfo()
    elif(N==6):
        branch.branchbase()
    elif(N==7):
        branch.branchmore()
    elif(N==8):
        branch.branchcondition()
