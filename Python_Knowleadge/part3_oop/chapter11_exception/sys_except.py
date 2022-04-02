# -*- coding:utf-8 -*-
"""
DateTime    :2022/4/2 11:04:01
Author      :chuanming
File        :sys_except
Description :系统异常处理
*Copyright @ chuanming 2022. All rights reserved
"""

def exceptionsingle():
    """单一的异常捕获"""
    try:
        result=3/0
        print("This is never been called")
    except:
        print("Exception happend !")
    finally:
        print("Process finished !")

def exceptionmore():
    """多异常捕获"""
    try:
        myList=[4,6]
        print(f"获取mylist第10位的内容{mylist[10]}")
        print("This is never been called")
    except ZeroDivisionError as e:
        print("Exception happend")
        print(f"{e}")
    except (IndexError,EOFError) as e:
        print("Exception happend")
        print(f"{e}")
    except:
        print("Unknown exception happend")
    else:
        print("No exception happend !")
    finally:
        print("Process finished ！")