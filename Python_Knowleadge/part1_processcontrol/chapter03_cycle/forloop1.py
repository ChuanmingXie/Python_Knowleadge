# -*- coding:utf-8 -*-

"""
DateTime    :2021/8/4 9:40
Author      :chuanmingxie
File        :forloop1.py
Software    :visual studio
Description :for循环的三种格式 | 集合枚举技巧
"""
import random

# 1. for循环的三种格式
counters = [0] * 6
for _ in range(6000):
    face = random.randint(1, 6)
    counters[face - 1] += 1

# 1.1. range(start,stop,step)
for i in range(1, 7):
    print(f'点数{i}出现了{counters[i - 1]}次')

# 1.2. range(len)
for i in range(len(counters)):
    print(f'点数{i + 1}出现了{counters[i]}次')

# 1.3. enumerate
for index, values in enumerate(counters):
    print(f'点数{index + 1}出现了{values}次')

# 2. 集合枚举技巧
# 正确
user1_list = ['刘德华', '范伟', '刘老根', '刘老四', '宋小宝', '刘能']
for index in range(len(user1_list) - 1, -1, -1):
    print(index, user1_list[index])
    item = user1_list[index]
    if item.startswith('刘'):
        user1_list.remove(item)
print(user1_list)

# 错误方式 1
user_list = ['刘德华', '范伟', '刘老根', '刘老四', '宋小宝', '刘能']
for item in user_list:
    print(item)
    if item.startswith('刘'):
        user_list.remove(item)
print(user_list)

# 错误方式 2
user2_list = ['刘德华', '范伟', '刘老根', '刘老四', '宋小宝', '刘能']
for i in range(0, len(user2_list)):
    print(i, user2_list[i])
    item = user2_list[i]
    if item.startswith('刘'):
        user2_list.remove(item)
print(user2_list)
