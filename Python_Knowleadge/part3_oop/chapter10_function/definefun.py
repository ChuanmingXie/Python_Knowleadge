# -*- coding:utf-8 -*-
"""
DateTime    :2022/4/1 21:32:13
Author      :chuanming
File        :definefun
Description :
*Copyright @ chuanming 2022. All rights reserved
"""
import datetime

def sum(x,y):return x+y

def total(x,y,z):
    """可以返回两个值"""
    sum_of_two=sum(x,y)
    sum_of_three=sum(sum_of_two,z)
    return sum_of_two,sum_of_three

def fundefinemain():
    """函数的定义和演示"""
    print(f"return of sum:{sum(4,6)}")
    x,y=total(1,7,10)
    print(f"return of total:{x},{y}")



def sumdefault(x,y=10):return x+y

def defaultparam():
    """默认参数函数"""
    print(f"return of sum(2,3):{sumdefault(2,3)}")
    print(f"return of sum(-4):{sumdefault(-4)}")

def paramorder():
    """参数传递顺序"""
    print(f"return of sum(1,2,3):{total(1,2,3)}")
    print(f"return of sum(y=2,z=3,x=1):{total(y=2,z=3,x=1)}")

    

def tuplevarlength(message,*tupleName):
    """元组变长函数,无需知道参数名称"""
    for name in tupleName:
        print(f"{message},{name}")

def dictvarlength(**dictParam):
    """字典变长函数,需要知道参数名称"""
    if(dictParam.get('Price')):
        price=int(dictParam['Price'])
        if price>100:
            print("*********I want buy this book*********")
        print("This book information are as follow:")
        for key in dictParam.keys():
            print(f"{key}:{dictParam[key]}")
        print("")

def variablelength():
    """使用变长函数"""
    tuplevarlength("Good morning","CloudWhales","Jack","Evans","zion",893,"Rose Hasa")
    dictvarlength(author='James',Title="经济学导论")
    dictvarlength(author='Linda',Title="深入Python",Date="2016-1-1",Price=203)
    dictvarlength(Date='2008-2-03',Title="家常菜普",Price=20)
    dictvarlength(author='Jinker Landy',Title="如何保持身材")
    dictvarlength(author='Finance',Name="公司高管的选择",Price=302)


def namedfunc(a):return "I'm named function with param %s" % a

def callfunc(func,param):
    print(datetime.datetime.now())
    print(func(param))
    print("")

def lambdamainfun():
    callfunc(namedfunc,"Hello")
    callfunc(lambda x:x*2,9)
    callfunc(lambda y:y*y,-4)
    print((lambda x,y:x-y)(3,4))