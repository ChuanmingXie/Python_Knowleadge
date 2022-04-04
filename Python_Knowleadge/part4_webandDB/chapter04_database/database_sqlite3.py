# -*- coding:utf-8 -*-
"""
DateTime    :2022/4/4 17:55:01
Author      :chuanming
File        :database_sqlite3
Description :使用SQlite3数据库
*Copyright @ chuanming 2022. All rights reserved
"""

import sqlite3

def SQLiteDB():
    """测试SQLite3数据库的使用"""
    conn=sqlite3.connect('test.db')
    # 获取游标对象
    cur=conn.cursor()
    # 执行一系列SQL语句
    # 建立一张表
    cur.execute("CREATE TABLE demo(num int,strinfo varchar(20));")
    # 插入一些记录
    cur.execute("INSERT INTO demo VALUES(%d,'%s')" %(1,'aaa'))
    cur.execute("INSERT INTO demo VALUES(%d,'%s')" %(2,'bbb'))
    cur.execute("INSERT INTO demo VALUES(%d,'%s')" %(3,'ccc'))
    cur.execute("INSERT INTO demo VALUES(%d,'%s')" %(4,'ddd'))
    # 更新一条记录
    cur.execute("UPDATE demo SET strinfo='%s' WHERE num=%d"%('fff',3))
    # 查询全部记录
    cur.execute("SELECT * FROM demo;")
    rows=cur.fetchall()
    print("记录数据条数：",len(rows))
    for i in rows:
        print(i)
    # 提交事务
    conn.commit()
    # 关闭游标对象
    cur.close()
    # 关闭数据库连接
    conn.close()

def T_SQL():
    """重点掌握的SQL语句"""
    #INSERT INTO 
