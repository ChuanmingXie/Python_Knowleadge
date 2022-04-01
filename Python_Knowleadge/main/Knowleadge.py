#-*- coding:utf-8 -*-

import time
import sys,os

# __file__获取执行文件相对路径，整行为取上一级的上一级目录
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 添加路径，这个是临时的
sys.path.append(base_dir+"\\part1_processcontrol")
sys.path.append(base_dir+"\\part2_datatypeuse")

from processcontrol import studyprint
from usedatatype import studydatatype

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def fbis(num):
    """斐波那契数列"""
    result=[0,1]
    for x in range(num-2):
        result.append(result[-2]+result[-1])
    return result

def main():
    result=fbis(10)
    fobj=open('D:\\CodePractice\\Backend\\Python\\result.txt','w+')
    for i,num in enumerate(result):
        print ("第 %d 个数是: %d "%(i,num))
        fobj.write("%d "%num)
        time.sleep(1)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Visual Studio 2019 for Python')
    callback='Y';
    while(callback.upper()!="N"):
        os.system("cls")
        print("测试算法如下")
        print("-------------1.流程控制语句-------------")
        print("-------------2.数据类型定义-------------")
        print("****************************************")
        N=int(input("请选择演示类别："))
        if(N==1):
            studyprint()
        elif(N==2):
            studydatatype()
        callback=input("你还要继续测试吗:N/Y ?")        
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
