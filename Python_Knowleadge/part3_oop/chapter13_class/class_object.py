# -*- coding:utf-8 -*-
"""
DateTime    :2022/4/2 11:25:19
Author      :chuanming
File        :class_object
Description :对象编程使用类
*Copyright @ chuanming 2022. All rights reserved
"""

class MyClass(object):
    """没有构造函数的类"""
    message="Hello,Developer."

    def show(self):
        print(f"内部消息：{self.message}")

def useclass():
    """使用普通类"""
    print(f"{MyClass.message}")
    MyClass.message="Good Morning !"
    print(f"{MyClass.message}")
    inst=MyClass()
    inst.show()
    print("")

class ClassConstructor(object):
    """带有构造函数的类"""
    message='Hello,Developer !'
    def show(self):
        print(f"内部消息：{self.message}")
    def __init__(self):
        print("构造函数被调用!")

def useconstructor():
    """使用带有构造函数的类"""
    inst=ClassConstructor()
    inst.show()
    print("")

class ClassMoreConstructor(object):
    """带有多个参数的构造函数"""
    message='Hello,Developer !'
    def show(self):
        print(f"内部消息：{self.message}")
    def __init__(self,name="unset",color="black"):
        print(f"构造函数被调用!参数{name},{color}")

def usemoreconstructor():
    """使用带有多个参数的构造函数"""
    inst1=ClassMoreConstructor()
    inst1.show()
    inst2=ClassMoreConstructor("David")
    inst2.show()
    inst3=ClassMoreConstructor("Lisa","Yellow")
    inst3.show()
    inst4=ClassMoreConstructor(color="Green")
    inst4.show()
    #错误示例演示
    #inst5=ClassMoreConstructor("Jerry","Yellow",color="Green")
    #inst5.show()
    print("")

class ClassDestructor():
    """带有析构函数的类"""
    message='Hello,Developer !'
    def show(self):
        print(f"内部消息：{self.message}")
    def __init__(self,name="unset",color="black"):
        print(f"构造函数被调用!参数{name},{color}")
    def __del__(self):
        print(f"析构函数被调用！")

def usedestructor():
    """使用带析构函数的类"""
    inst1=ClassDestructor()
    inst1.show()
    inst2=ClassDestructor()
    inst2.show()
    del inst1,inst2
    inst3=ClassMoreConstructor("Lisa","Yellow")
    inst3.show()
    del inst3
    print("")

class ClassUseMember(object):
    """定义具有成员变量的类"""
    message='Hello,Developer.'
    def show(self):
        print(f"{self.message}")
        print(f"Here is {self.name} in {self.color}")
    def __init__(self, name="unset",color="black"):
        print(f"构造函数被调用参数有：{name},{color}")
        self.name=name
        self.color=color
    def __del__(self):
        print(f"析构函数被调用{self.name}")

def usemember():
    """使用具有成员变量的类"""
    inst1=ClassUseMember("David")
    inst1.show()
    print(f"inst1的颜色{inst1.color}")
    
    inst2=ClassUseMember("David","Yellow")
    inst2.show()
    print(f"inst2的名称{inst2.name}")
    del inst1,inst2
    print("")

class ClassStaticFun():
    """定义静态函数和类函数"""
    message="Hello,Developer !"
    def show(self):
        print(f"{self.message}")
        print(f"Here is {self.name} in {self.color}")
    @staticmethod
    def printmessage():
        print("printMeaage 方法被调用")
        print(f"{ClassStaticFun.message}")
    @classmethod
    def createObject(cls,name,color):
        print(f"对象将会被创建：{cls.__name__},{name},{color}")
        return cls(name,color)
    def __init__(self, name="unset", color="black"):
        print(f"构造函数被调用参数：{name},{color}")
        self.name=name
        self.color=color
    def __del__(self):
        print(f"析构函数被调用{self.name}")

def useStaticMethod():
    """使用静态函数和类函数"""
    ClassStaticFun.printmessage()
    inst=ClassStaticFun.createObject("Toby","Red")
    print(f"{inst.message}")
    del inst
    print("")

class ClassUsePrivate(object):
    """定义带有私有成员的类"""
    def __init__(self, *args, **kwargs):
        #print("构造函数被调用，参数是：{kwargs.get('name')},{kwargs.get('color')}")
        print(f"构造函数被调用, 参数是：{kwargs['name']},{kwargs['color']}")
        self.__message=args
        self.__name=kwargs['name']
        self.__color=kwargs['color']
    def __del__(self):
        print(f"析构函数被调用{self.__message}")
        print(f"析构函数被调用{self.__name}")
        print(f"析构函数被调用{self.__color}")

def usePrivate():
    """使用带有滴油成员的类"""
    inst=ClassUsePrivate("tuple类型的参数1","tuple类型参数2",name="Jojo",color="White")
    del inst
    print("")
