#-*- coding:utf-8 -*-

import time

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))    #__file__获取执行文件相对路径，整行为取上一级的上一级目录
sys.path.append(BASE_DIR+"\\chapter02：Python顺序语句")   #添加路径，这个是临时的

from Chapter01Print import StudyPrint

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
    print_hi('Visual Stdio 2019 for Python')
    StudyPrint()
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
