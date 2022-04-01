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
sys.path.append(base_dir+"\\part1_processcontrol\\chapter03_cycle")

import orderinput,orderprint,branch,condition,judge,forloop1,forloop2,nestedloop,whileloop1,whileloop2

def studyprint():
    os.system("cls")
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
    print("****************************************")
    print("-------------09.长度单位转换------------")
    print("-------------10.分数等级转换------------")
    print("-------------11.分段函数转换------------")
    print("-------------12.色子决定事情------------")
    print("-------------13.报税系统使用------------")
    print("-------------14.验证用户身份------------")
    print("-------------15.三角形的验证------------")
    print("****************************************")    
    print("-------------16.for  循环---------------")
    print("-------------17.while循环---------------")
    print("-------------18.嵌套 循环---------------")

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
    elif(N==9):
        condition.lengthunit()
    elif(N==10):
        condition.scorejudge()
    elif(N==11):
        condition.sectionfun()
    elif(N==12):
        condition.decisiondowhat()
    elif(N==13):
        condition.taxsystem()
    elif(N==14):
        condition.validationuser()
    elif(N==15):
        condition.trianglejudge()
    elif(N==16):
        forloop1.forenum()
        forloop1.gathernum()
        forloop2.oddsum()
        forloop2.printtriangle()
        forloop2.judgeprime()
        forloop2.multitable()
    elif(N==17):
        whileloop1.loopnum()
        whileloop1.looplogin()
        whileloop1.whileelse()
        whileloop2.printhundred()
        whileloop2.printten()
        whileloop2.sumhundred()
        whileloop2.oddoreven()
        whileloop2.printnumber()
    elif(N==18):
        nestedloop.guessnumberbase()
        nestedloop.guessnumber()
        nestedloop.guessnumberpro()
