# -*- coding:utf-8 -*-

"""
DateTime    :2021/8/1 19:01
Author      :chuanmingxie
File        :06_字符串格式化.py
Software    :PyCharm
Description :
"""
# 1.%
# 字符串格式化
from timeit import timeit

name = '谢传明'
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

# 格式化
print('%+10x' % 11)  # 输出整数11 对应的16进制字符串，会出现异常 + 号
print('%04d' % 5)  # 输出整数 5 且左侧填充0补齐4位
print('%6.3f' % 2.3)  # 输出浮点数2.3 且精度位3小数点后3位
print("%-10x" % 10)  # 输出整数10 对应的16进制字符串,且左对齐补齐10位
print("% 10x" % 10)  # 输出整数10 对应的16进制字符串,且左侧补0对齐10位

print('{0:+10x}'.format(10))  # 输出整数11 对应的16进制字符串
print('{0:04d}'.format(5))  # 输出整数 5 且左侧填充0补齐4位
print('{0:6.3f}'.format(2.3))  # 输出浮点数2.3 且精度位3小数点后3位
print('{0:10x}'.format(10))  # 输出整数10 对应的16进制字符串,

# 进制转化
print('%o' % 10)  # 输出整数为10的8进制数
print('%x' % 10)  # 输出整数为10的16进制
print('%x' % 20)  # 输出整数为20的16进制
for num in range(0, 20, 1):
    # print(f'{num}   {bin(num)}  {oct(num)}  {hex(num)}')
    print("{0:06b}    {1:4o}   {2:4x}".format(num, num, num))

# 浮点数输出
print('%f' % 1.11)  # 默认保留6为小数
print('%.1f' % 1.11)  # 取1位小数
print('%e' % 1.11)  # 默认6位小数，可学计数法
print('%.3e' % 1.11)  # 取三位小数,科学计数法
print('%g' % 1111.1111)  # 默认6位有效位数
print('%.7g' % 1111.1111)  # 取7位有效位数
print('%.2g' % 1111.1111)  # 取2位有效数字,自动转化为科学计数法

# 字符串输出
print('%s' % 'hello world')  # 普通的字符输出
print('%20s' % 'hello world')  # 右对齐，取20位，不够则补0
print('%-20s' % 'hello world')  # 左对齐，取20位，不够则补0
print('%.2s' % 'hello world')  # 取2位
print('%10.2s' % 'hello world')  # 右对齐，取2位
print('%-10.2s' % 'hello world')  # 左对齐，取2位

# 2.format
# 填充与格式化
print('{0:*<10}'.format('谢传明'))  # 以*号结束
print('{0:*>10}'.format('谢传明'))  # 以*号开头
print('{0:*^10}'.format('谢传明'))  # *号置于开头结尾

# 精度与进度
print('{0:.2f}'.format(1232132.12321))  # 精确到小数点后两位
print('{0:b}'.format(10))  # 二进制
print('{0:o}'.format(10))  # 十进制
print('{0:x}'.format(10))  # 十六进制
print('{0:,}'.format(123232244324))  # 千分位格式化

# 使用索引
l1 = ['谢传明', 27]
l2 = ['hobby', '冥想']
print('{0[0]}age is {0[1]},{1[0]}is{1[1]}'.format(l1, l2))

# 3.f-string
# 3.1.字符输出
name = '谢传明'
age = 18
job = '学生'
hobby = '篮球'
print(f'我叫{name}，我的年龄是{age}，我是一名{job}，我的爱好是{hobby}')

# 3.2.进制转换
print(f"小明今年{22}岁")
print(f"小明今年{22:#b}岁")
print(f"小明今年{22:#o}岁")
print(f"小明今年{22:#x}岁")

# 3.3.填充与格式化
print(f'{name:*<10}')
print(f'{name:*>10}')
print(f'{name:*^10}')
# 3.4.运算表达式
text = f"小明的名字叫喵喵，今年{19 + 2}岁"
print(text)
print(f'{2 ** 3 + 1}')


class People(object):
    # 使用类调用字符串
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age}'

    def __repr__(self):
        return f'{self.name} is {self.age} HaHA!'


XCM = People('chuangmingxie', 24)
print(F'{XCM}')
print(F'{XCM!r}')
print(XCM)

name = 'chuanmingxie'
age = 27
status = 'Python'
message = {
    f'hi {name}'
    f'you are {age}'
    f'you are learning {status}'
}
print(message)


# 使用各方法的速度比较
def test_baifeihaotime():
    name = 'chuanmingxie'
    age = 27
    return '%s is %s .' % (name, age)


def test_formattime():
    name = 'chuanmingxie'
    age = 27
    return '{} is {}.'.format(name, age)


def test_f_stringtime():
    name = 'chuanmingxie'
    age = 27
    return f'{name} is {age}.'


print(timeit(test_baifeihaotime, number=1000000))
print(timeit(test_formattime, number=1000000))
print(timeit(test_f_stringtime, number=1000000))
