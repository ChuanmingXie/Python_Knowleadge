# -*- coding:utf-8 -*-

"""
DateTime    :2021/8/1 18:12
Author      :chuanmingxie
File        :orderoutput.py
Software    :visual studio
Description :顺序执行输出
"""
import getpass

def buddhistimg():
    """打印佛像"""
    print("                           _ooOoo_  ")
    print("                          o8888888o  ")
    print("                          88  .  88  ")
    print("                          (| -_- |)  ")
    print("                           O\\ = /O  ")
    print("                       ____/`---'\\____  ")
    print("                     .   ' \\| |// `.  ")
    print("                      / \\||| : |||// \\  ")
    print("                    / _||||| -:- |||||- \\  ")
    print("                      | | \\\\\\ - /// | |  ")
    print("                    | \\_| ''\\---/'' | |  ")
    print("                     \\ .-\\__ `-` ___/-. /  ")
    print("                  ___`. .' /--.--\\ `. . __  ")
    print("               ."" '< `.___\\_<|>_/___.' >'"".  ")
    print("              | | : `- \\`.;`\\ _ /`;.`/ - ` : | |  ")
    print("                \\ \\ `-. \\_ __\\ /__ _/ .-` / /  ")
    print("        ======`-.____`-.___\\_____/___.-`____.-'======  ")
    print("                           `=---='  ")
    print("  ")

def printverse1():
    """打印小诗1"""
    print("                 佛祖镇楼                 BUG辟易  ")
    print("         佛曰:  ")
    print("                 写字楼里写字间，写字间里程序员；  ")
    print("                 程序人员写程序，又拿程序换酒钱。  ")
    print("                 酒醒只在网上坐，酒醉还来网下眠；  ")
    print("                 酒醉酒醒日复日，网上网下年复年。  ")
    print("                 但愿老死电脑间，不愿鞠躬老板前；  ")
    print("                 奔驰宝马贵者趣，公交自行程序员。  ")
    print("                 别人笑我忒疯癫，我笑自己命太贱；  ")
    print("                 不见满街漂亮妹，哪个归得程序员？")

def printverse2():
    """打印小诗2"""
    print('何当共剪西窗烛', end = ',')
    print('却话巴山夜雨时', end = '.')
    print()

def printverse3():
    """打印小诗3"""
    print('     商山早行    ')
    print('             唐 温庭筠')
    print('晨起动征铎', end=',')
    print('客行悲故乡。')
    print('鸡声茅店月', end=',')
    print('人迹板桥霜。')
    print('胡叶落山路', end=',')
    print('枳花明译墙。')
    print('因思杜陵梦', end=',')
    print('凫雁满回塘。')
    print()

def printuser():
    name = input('请输入您的姓名:')
    sex = input('请输入您的性别:')
    password = input('请输入密码:')
    # password=getpass.getpass('Password')
    print(name, password)

def welcomeuser():
    # 1. 提示输出姓名，给出欢迎提示
    name = input('用户名：')
    print(name + '欢迎您 ！')

    # 2. 提示输入姓名|位置|行为, 然后拼接显示
    name = input('请输入姓名:')
    position = input('请输入您所在位置:')
    action = input('请说明您的行动:')
    print(name + '在' + position + action)
