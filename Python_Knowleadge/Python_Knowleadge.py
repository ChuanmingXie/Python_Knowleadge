# This is a sample Python script.
#-*- coding:utf-8 -*-
import time
import sys 
sys.path.append(".\chapter02：Python顺序语句\Chapter01Print.py") 
import Chapter01Print

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
    main()
    Chapter01Print.StudyPrint()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
