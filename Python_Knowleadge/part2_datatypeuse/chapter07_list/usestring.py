# -*- coding:utf-8 -*-
"""
DateTime    :2022/4/1 19:50:48
Author      :chuanming
File        :usestring
Description :String类型数据使用
*Copyright @ chuanming 2022. All rights reserved
"""

def usebase():
    print(f"Hello, World !")
    print(u"Hello, I'm Unicode !")
    print(u"你好, 世界")
    print(f"你好, 世界")
    a="Hello, World !"
    print(f"{a}读取位置5的元素={a[5]}")
    print(f"{a}读取字符串从7到最后的位置=a[7:]")
    a+=" I like Python ！"
    print(f"{a}")
    print(f"删除中间的部分内容={a[:6]+a[-8:]}")

def useformat():
    #print(f"charA={char(A)}")
    #print(f"charB={char(B)}")
    #print(u"ASCII码65代表：%c" % char(A))
    #print(u"ASCII吗%d代表：B" % char(B))

    print("%#x" % 108)
    print('%E' % 1234.567890)
    print("Host:%s\t Port:%d" % ('python',80))
    print("MM/DD/YY=%02d/%02d/%d" % (2,1,97))

    print("Hi，\nToday is Friday")
    print(r"Hi, \ntoday is Friday")

def useinnerfun():
    a="hello,world"
    #print(f"{a}的capitalize={capitalize(a)}")
    print(f"{a}的title化={a.title()}")
    print(f"{a}的split后={a.split()}")