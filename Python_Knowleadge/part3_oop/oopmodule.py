# -*- coding:utf-8 -*-
"""
DateTime    :2022/4/1 22:21:26
Author      :chuanming
File        :oopmodule
Description :
*Copyright @ chuanming 2022. All rights reserved
"""

import sys,os
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir+"\\part3_oop\\chapter09_basictrain")
sys.path.append(base_dir+"\\part3_oop\\chapter10_function")
sys.path.append(base_dir+"\\part3_oop\\chapter11_exception")
sys.path.append(base_dir+"\\part3_oop\\chapter12_file")
sys.path.append(base_dir+"\\part3_oop\\chapter13_class")

import conditionproc,loopprocess
import definefun,sys_except,user_except
import getfilepath,class_object,class_inherit

def studyoop():
    """面向对象测试"""
    os.system("cls")
    print("请选择演示算法")
    print("-------------1.基础综合训练-------------")
    print("-------------2.函数定义使用-------------")
    print("-------------3.异常捕获定义-------------")
    print("-------------4.文件使用操作-------------")
    print("-------------5.对象及类文件-------------")

    N=int(input("请选择演示类别："))
    if(N==1):
        loopprocess.whileappend()
        loopprocess.whileRange()

        conditionproc.condationreplace()
        conditionproc.validationuser()
        conditionproc.conditionjudge()
    if(N==2):
        definefun.fundefinemain()
        definefun.defaultparam()
        definefun.paramorder()
        definefun.variablelength()
        definefun.lambdamainfun()
    if(N==3):
        sys_except.exceptionsingle()
        sys_except.exceptionmore()
        user_except.userdefinemain()
    if(N==4):
        getfilepath.rootpath()
    if(N==5):
        class_object.useclass()
        class_object.useconstructor()
        class_object.usemoreconstructor()
        class_object.usedestructor()
        class_object.usemember()
        class_object.useStaticMethod()
        class_object.usePrivate()
        class_inherit.useInherit()
        class_inherit.useMoreInherit()
