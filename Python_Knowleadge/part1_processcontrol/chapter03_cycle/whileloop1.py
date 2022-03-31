# -*- coding:utf-8 -*-

"""
DateTime    :2021/8/1 21:29
Author      :chuanmingxie
File        :whileloop1.py
Software    :visual studio
Description :while循环
"""

# 1. 死循环
# while True:
#     print('今天下午学python,真高兴啊 !')

# while 判断条件(condition):  # 自动将表达式的值会直接转为布尔类型 即会判断 bool(表达式) 的值
#     执行语句(statements).. # 当值为True时，会执行循环体，否则退出循环
#
# while 条件:
#     满足条件的时候执行的事情

# 2. 设定循环次数
num = 1
while num < 4:
    print('我爱你中国')
    num = num + 1

# 3. 中止While循环的两种方式
print('开始运行超级无敌系统')

while True:
    user = input('请输入用户名:')
    pwd = input('请输入密码:')
    if user == 'chuanmingxie' and pwd == '666666':
        print('登录成功')
        break
    else:
        print('用户名或密码错误')

print('开始运行超级无敌系统')
flag = True
while flag:
    user = input('请输入用户名:')
    pwd = input('请输入密码:')
    if user == 'chuanmingxie' and pwd == '666666':
        print('登陆成功')
        flag = False
    else:
        print('用户名或密码错误')

# 4. 限制用户登录次数  while...else
num = 3
while num > 0:
    num -= 1
    name = input('请输入用户名:')
    pwd = input('请输入密码:')
    if name == 'siwei' and pwd == '123456':
        print('输入正确')
        break
    print(f'用户名或密码错误,请重新输入,还剩{num}次机会')
else:
    print('错误超过三次,请一个小时后再试 !')

num = 1
while num <= 3:
    name = input('请输入用户名:')
    pwd = input('请输入密码:')
    if name =='嘉兴' and pwd =='123456':
        print('输入正确')
        break
    print(f'用户名或密码错误,请重新输入,还有{3-num}次机会')
else:
    print('密码输入错误超过三次,请一小时后再试')


