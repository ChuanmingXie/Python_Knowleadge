# -*- coding:utf-8 -*-
"""
DateTime    :2022/4/1 20:16:22
Author      :chuanming
File        :uselist
Description :
*Copyright @ chuanming 2022. All rights reserved
"""

def listarray():
    """list基础应用"""
    mylist=['you',456,'English',9.34]
    print(f"{mylist}获取第三个元素={mylist[2]}")
    mylist[2]='chinese'
    print(f"更新后的{mylist}")
    print(f"{mylist}的长度{len(mylist)}")
    numlist=[2,8,16,1,-6,53,-1]
    print(f"{numlist}排序后={sorted(numlist)}")
    print(f"{numlist}本身并不变化")
    print(f"{numlist}求和={sum(numlist)}")

def listinnerfun():
    """list内部函数"""
    numlist=[2,8,16,8,-6,52,-1]
    print(f"{numlist}中8的个数={numlist.count(8)}")
    print(f"{numlist}第二位插入数据9={numlist.insert(1,9)}")
    print(f"{numlist}")

def listappend():
    """列表的追加"""
    welcome="欢迎使用WT游戏".center(30,"*")   #格式文本30字符,两边补齐"*"
    print(welcome)
    user_count=0
    while True:
        count=input("请输入游戏人数：")
        if count.isdecimal():
            user_count=int(count)
            break
        else:
            print("输入格式错误,人数必须是数字")
    message="{}人参加WT游戏".format(user_count)
    print(message)

    user_name_list=[]
    for i in range(1,user_count+1):
        tips="请输入玩家姓名（{}/{}）：".format(i, user_count)
        name=input(tips)
        user_name_list.append(name)
    print(user_name_list)

def listdelete():
    """列表元素的删除"""
    #不能在循环的过程中，边循环获取列表的数据 边删除列表的数据，需要倒这处理。
    user_list=['刘德华','张学友','刘能','宋小宝','赵敏']
    for index in range(len(user_list) - 1, -1, -1):
        #5 4 3 2 1 0
        item=user_list[index]
        if item.startswith("刘"):
            user_list.remove(item)
    print(user_list)

def listsorted():
    """列表排序"""
    num_list=[11,22,33,2,5,11,99,88]
    print(num_list)
    num_list.sort()                 # num_list从小到大排序
    num_list.sort(reverse=True)     # num_list从大到小排序
    print(num_list)

    user_list=['贾宝玉','x薛宝钗','王熙凤','Ab石头记','1',23]
    print(user_list)

def unicodelist():
    """获取unicode表示"""
    data="1"
    data_list=[]
    for char in data:
        v1 = ord(char)
        data_list.append(v1)

    print(data)
    print(data_list)