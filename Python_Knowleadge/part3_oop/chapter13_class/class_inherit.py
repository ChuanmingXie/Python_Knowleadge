# -*- coding:utf-8 -*-
"""
DateTime    :2022/4/2 19:27:26
Author      :chuanming
File        :class_inherit
Description :面向对象继承的设计
*Copyright @ chuanming 2022. All rights reserved
"""

#class BaseClass(object):
#    block_class

#class SubClass(BaseClass):
#    block_class

class Base(object):
    """父类"""
    def __init__(self, *args, **kwargs):
        print("基本类构造函数被调用！")
    def __del__(self):
        print("基本类析构函数被调用！")
    def move(self):
        print(f"基本类的move的函数被调用！")

class SubA(Base):
    """子类"""
    def __init__(self, *args, **kwargs):
        print("SubA子类被调用!")
    def move(self):
        print("SubA子类的move函数被调用！")

class SubB(Base):
    """子类"""
    def __del__(self):
        print("SubB子类的析构函数被调用！")
        super().__del__()

def useInherit():
    """继承类的使用"""
    instA=SubA()
    instA.move()
    del instA
    print("---------------------------")
    instB=SubB()
    instB.move()
    del instB
    print("")


class BaseA(object):
    def move(self):
        print(f"父类A的move被调用 ！")

        
class BaseB(object):
    def move(self):
        print(f"父类B的move被调用 ！")

        
class BaseC(BaseA):
    def move(self):
        print(f"父类C的move被调用 ！")

class Sub(BaseC,BaseB):
    pass

def useMoreInherit():
    """都继承的使用:Sub、BaseC、BaseA、BaseB"""
    inst=Sub()
    inst.move()