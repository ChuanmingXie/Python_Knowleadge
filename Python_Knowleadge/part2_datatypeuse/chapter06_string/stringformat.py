# -*- coding:utf-8 -*-
"""
DateTime    :2022/3/31 15:38:45
Author      :chuanming
File        :stringformat
Description :
*Copyright @ chuanming 2022. All rights reserved
"""

def occupyformat():
    name = '诸葛孔明'
    age = 18
    job = '学生'
    hobby = '篮球'

    # 输出方式1:
    print('我的名字是%s,年龄%d,职业%s,爱好%s' % (name, age, job, hobby))
    # 输出方式2:
    # 使用位置参数
    print('我的名字{},年龄{},职业{},爱好{}'.format(name, age, job, hobby))
    print('我的名字{0},年龄{1},职业{2},爱好{3}'.format(name, age, job, hobby))

    # 字典格式化时，指定格式化字符的时候位置可以调换
    print('我叫{name},年龄{age},职业{job},爱好{hobby}'
          .format(name=name, age=age, job=job, hobby=hobby))
    print('hello {name}, you sex is {sex}.'.format(sex='boy', name='tab'))
    args = {'name': 'tab', 'sex': 'boy'}
    print('hello {name}, you sex is {sex}.'.format(**args))
    
    # 字符串输出
    print('%s' % 'hello world')  # 普通的字符输出
    print('%20s' % 'hello world')  # 右对齐，取20位，不够则补0
    print('%-20s' % 'hello world')  # 左对齐，取20位，不够则补0
    print('%.2s' % 'hello world')  # 取2位
    print('%10.2s' % 'hello world')  # 右对齐，取2位
    print('%-10.2s' % 'hello world')  # 左对齐，取2位

    # 以*号结束
    print('{0:*<10}'.format('诸葛孔明'))
    # 以*号开头
    print('{0:*>10}'.format('诸葛孔明'))
    # *号置于开头结尾
    print('{0:*^10}'.format('诸葛孔明'))

def fformat():
    # 使用索引
    l1 = ['诸葛孔明', 27]
    l2 = ['hobby', '冥想']
    print('{0[0]}age is {0[1]},{1[0]}is{1[1]}'.format(l1, l2))

    # 3.f-string
    # 3.1.字符输出
    name = '诸葛孔明'
    age = 18
    job = '学生'
    hobby = '篮球'
    print(f'我叫{name}，我的年龄是{age}，我是一名{job}，我的爱好是{hobby}')

    # 3.3.填充与格式化
    print(f'{name:*<10}')
    print(f'{name:*>10}')
    print(f'{name:*^10}')

    # 3.4.运算表达式
    text = f"小明的名字叫喵喵，今年{19 + 2}岁"
    print(text)

class people(object):
    # 使用类调用字符串
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age}'

    def __repr__(self):
        return f'{self.name} is {self.age} HaHA!'

def formatinclass():
    username=people('cloudwhales',24)
    print(F'{username}')
    print(F'{username!r}')
    print(username)

def formatinstruct():
    name="CloudWhales"
    age = 27
    status = 'Python'
    message = {
        f'hi {name}'
        f'you are {age}'
        f'you are learning {status}'
    }
    print(message)