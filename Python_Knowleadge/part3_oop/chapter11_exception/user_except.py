# -*- coding:utf-8 -*-
"""
DateTime    :2022/4/2 11:04:17
Author      :chuanming
File        :user_except
Description :
*Copyright @ chuanming 2022. All rights reserved
"""

import sys

class MyError(Exception):
    def __str__(self):
        return "I'm a self-defined Error!"

def userdefinemain():
    try:
        print(f"***************Strat of mian()***************")
        if(len(sys.argv)==1):
            raise MyError()
        print(f"****************End of mian()****************")

    except e as MyError:
        print(f"{e}")
