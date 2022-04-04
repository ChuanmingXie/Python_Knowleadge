# -*- coding:utf-8 -*-
"""
DateTime    :2022/4/4 18:06:45
Author      :chuanming
File        :BBAndORM
Description :
*Copyright @ chuanming 2022. All rights reserved
"""
import sys,os
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir+"\\part4_webanddb\\chapter04_database")
sys.path.append(base_dir+"\\part4_webanddb\\chapter03_webclient")

import database_sqlite3

def studydatabase():
    """面向对象测试"""
    os.system("cls")
    print("请选择演示算法")
    print("-------------1.基础综合训练-------------")

    N=int(input("请选择演示类别："))
    if(N==1):
        database_sqlite3.SQLiteDB()