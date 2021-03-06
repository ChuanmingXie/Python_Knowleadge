# -*- coding:utf-8 -*-

"""
DateTime    :2021/8/4 9:40
Author      :chuanmingxie
File        :nestedloop.py
Software    :visual studio
Description :嵌套循套的猜数游戏
"""
import random


def guessnumberbase():
    '''猜数字'''
    numReady = 66
    while True:
        numGuass = int(input('请输入数字:'))
        if numGuass == numReady:
            print('恭喜你，输入正确')
            break
        elif numGuass < numReady:
            print('你输入的数字小了')
        else:
            print('你输入的数字大了')

def guessnumber():
    """while True"""
    num = random.randint(1, 100)
    times = 1
    while True:
        num2 = int(input('请输入数字【1-100】(共10次机会):'))
        if times > 10:
            print(f'很遗憾，游戏结束，正确数字是{num2}，请下次再试')
            break
        if num2 == num:
            print('恭喜你，猜对了')
            break
        elif num2 < num:
            print(f'{num2}小了,请重新输入,你还剩{10 - times}次机会')
        else:
            print(f'{num2}大了,你重新输入,你还剩{10 - times}次机会')
        times += 1

def guessnumberpro():
    '''升级版猜数游戏'''
    total_times, times = 5, 1
    num = random.randint(1, 100)
    while True:
        num2 = int(input(f'请输入数字【1-100】(共{total_times}次机会):'))
        if num2 == num:
            print('恭喜你，答对了.')
            break
        elif num2 < num:
            if times != total_times:
                print(f'{num2}小了,请重新输入,您还剩{total_times - times}次机会')
            else:
                print(f'{num2}小了')
        else:
            if times != total_times:
                print(f'{num2}大了,请重新输入,您还剩{total_times - times}次机会')
            else:
                print(f'{num2}大了')
        times += 1
        if times > total_times:
            print('很遗憾,您的机会已经用完！')
            choice = input('您还想继续游戏吗？【Y|N】')
            if choice == 'Y':
                times = 1
                continue
            elif choice == 'N':
                print(f'已退出,正确数字是{num}')
                break
    print('程序已退出！')