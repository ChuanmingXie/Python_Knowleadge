# -*- coding:utf-8 -*-

"""
DateTime    :2021/8/4 9:40
Author      :chuanmingxie
File        :04_for练习.py
Software    :PyCharm
Description :
"""
from math import sqrt

'''1-100 之间的偶数求和'''
sumNumber = 0
for x in range(2, 100, 2):
    sumNumber += x
print(sumNumber)

sum1 = 0
for x in range(1, 100):
    if x % 2 == 0:
        sum1 += x
print(sum1)

'''打印三角形图案'''
row = int(input('请输入行数:'))

for i in range(row):
    for _ in range(i + 1):
        print('*', end='  ')
    print()
print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print('   ', end='')
        else:
            print('*', end='  ')
    print()
print()

for i in range(row):
    for _ in range(row - i - 1):
        print('   ', end='')
    for _ in range(2 * i + 1):
        print('*', end='  ')
    print()

'''判断素数'''
num = int(input('请输入一个正数:'))
if num == 1:
    print('1是素数')
else:
    end = int(sqrt(num))
    for x in range(2, end + 1):
        if num % x == 0:
            print(f'{num}不是素数')
            break
        else:
            print(f'{num}是素数')

'''9*9乘法表'''
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i}*{j}={i * j:<2}', end=' ')
    print()

"""
1 * 1 = 1
2 * 1 = 2 2 * 2 = 4
3 * 1 = 3 3 * 2 = 6 3 * 3 = 9
... 
"""

i = 1
while i <= 9:
    j = 1
    while j <= i:
        # print("%d*%d=%d\t" % (j, i, i * j), end=" ")
        print(f'{i}*{j}={i * j}\t', end=' ')
        # print(f'{i}*{j}={i*j:<2}', end=' ')
        j += 1
    print()
    i += 1
