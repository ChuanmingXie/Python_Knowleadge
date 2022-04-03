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

def nameSystem():
    """
    打印系统信息：欢迎使用XX系统...
    用列表存储用户的名字
    循环执行
        用户可以选择执行的具体操作
            名字的添加、删除、修改、查询操作
            按’q'选择退出
    打印退出信息，比如欢迎下次再来
    """
    # 打印系统信息
    print('='* 38)
    print('欢迎使用名字管理系统V0.1'.center(30))
    print('='* 38)
    
    # 创建一个列表，存放名字信息
    name_list=[]

    # 开启循环
    while True:
        # 1. 打印系统功能，获取用户名字信息
        print('系统功能：1.添加名字 2.修改名字 3.查询名字 4.删除名字 q.退出系统')
        choice=input('请选择：')
        if choice=='1':
            # 添加名字
            name=input('请输入要添加的名字【返回上一级请按 0】')
            if name=='0':
                continue
            elif name in name_list:
                print('这个名字已经添加过了！')
            else:
                name_list.append(name)
                print(f'{name} 添加成功')
        elif choice=='2':
            # 修改名字
            while True:
                old_name=input('请输入要修改的原名字【返回上一层请按 0】')
                if old_name=='0':
                    continue
                elif old_name not in name_list:
                    print('原名称不存在,请重新输入')
                    continue
                new_name=input('请重新输入要修改的名字')
                index=name_list.index(old_name)
                name_list[index]=new_name
                print(f"{new_name}名字修改成功 ！")
                break
            # 在旧名字所在位置插入新名字
            # name_list.insert(index,new_name)
            # 将旧名字删除
            #namename_list.remove(old_name)
        elif choice=='3':
            # 查询名字
            while True:
                count=len(name_list)
                print('1.查询一个名字【根据索引查询】 2.查询一个名字是否存在 3.查询所有名字 0.返回上一级')
                user_input=input('请选择：')
                if user_input=='1':
                    index = input(f"请输入查询索引【0-{count}】：")
                    if index.isdecimal():
                        index=int(index)
                    else:
                        print('您输入的数据类型有误,请重新输入')
                        continue
                    if index<count:
                        print(f"索引为{index}时 查询到的名字为 {name_list[index]}")
                        break
                    else:
                        print("您输入的索引超出范围,请重新输入")
                        break
                elif user_input=='2':
                    name=input(f"请输入查询的名字")
                    if name in name_list:
                        print(f"名字{name}存在")
                    else:
                        print(f"名字{name}不存在")
                    break
                elif user_input=='3':
                    print('名字列表:\n\t',end='')
                    for index,name in enumerate(name_list):
                        print(f"{index}:{name}",end=' ')
                    print()
                    break
                elif user_input=='0':
                    break
                else:
                    print('您的输入有误,请重新输入')
                    continue
        elif choice=='4':
            # 删除名字
            while True:
                name=input("请输入要删除的名字【返回上一级请按 0】")
                if name=='0':
                    break
                if name not in name_list:
                    print('名字不存在，请重新输入')
                    continue
                #删除名字
                name_list.remove(name)
                print(f'{name}已删除')
                break
        elif choice=='q':
            print('欢迎下次再次使用，祝您生活愉快！')
            break
        else:
            print('您的输入有误,请重新输入 ! ')

def cardsList():
    """
    生成一副扑克牌
    1.定义两个列表
        [黑桃, 梅花, 方块, 红桃]
        [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K,]
    2.定义一个空列表，存放纸牌
    3.循环嵌套两个列表
        每一次内层循环嵌套组合列表中的元素
        添加到结果列表中
    4.打印列表元素
    """
    colors=['黑桃', '梅花', '方块', '红桃']
    points=['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    cards=[f'{color}{point}' for point in points for color in colors]
    print(cards)