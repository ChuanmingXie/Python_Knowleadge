# -*- coding:utf-8 -*-
"""
DateTime    :2022/4/1 10:44:04
Author      :chuanming
File        :usedatatype
Description :
*Copyright @ chuanming 2022. All rights reserved
"""

import sys,os
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir+"\\part2_datatypeuse\\chapter04_number")
sys.path.append(base_dir+"\\part2_datatypeuse\\chapter05_binarycode")
sys.path.append(base_dir+"\\part2_datatypeuse\\chapter06_string")
sys.path.append(base_dir+"\\part2_datatypeuse\\chapter07_list")
sys.path.append(base_dir+"\\part2_datatypeuse\\chapter08_set")

import numberformat,numbertype,binary,encoding,formattime,stringformat,stringtype
import sequence,usestring,usetuple,uselist

def studydatatype():
    os.system("cls")
    print("请选择演示算法")
    print("-------------1.number数据类型-------------")
    print("-------------2.number的格式化-------------")
    print("******************************************")
    print("-------------3.进制的相互转换-------------")
    print("-------------4.数据的编码解码-------------")
    print("******************************************")
    print("-------------5.string数据类型-------------")
    print("-------------6.string的格式化-------------")
    print("-------------7.不同格式化用时-------------")
    print("******************************************")
    print("-------------8.sequence类型簇-------------")
    print("-------------9.string数据类型-------------")
    print("-------------10.tuple数据类型-------------")
    print("-------------11.list 数据类型-------------")

    N=int(input("请选择演示类别："))
    if(N==1):
        numbertype.numberclac()
        numbertype.numberconvert()
        numbertype.numbercommfun()
        numbertype.numberspecially()
    elif(N==2):
        numberformat.occupyformat()
    elif(N==3):
        binary.binaryconvert()
    elif(N==4):
        encoding.binencode()
        encoding.nameencode()
    elif(N==5):
        stringtype.stringuse()
        stringtype.stringsection()
        stringtype.stringfun()
    elif(N==6):
        stringformat.occupyformat()
        stringformat.f_format()
        stringformat.formatinclass()
        stringformat.formatinstruct()
    elif(N==7):
        formattime.timecompare()
    elif(N==8):
        sequence.commsequence()
        sequence.arraycomm()
    elif(N==9):
        usestring.usebase()
        usestring.useformat()
        usestring.useinnerfun()
    elif(N==10):
        usetuple.tuplearry()
    elif(N==11):
        uselist.listarray()
        uselist.listinnerfun()