# -*- coding:utf-8 -*-

"""
DateTime    :2021/8/4 21:14
Author      :chuanmingxie
File        :03_条件语句练习.py
Software    :PyCharm
Description :
"""
import math
import random

'''英制单位英寸和公制单位厘米的互换'''
value = float(input('请输入长度:'))
unit = input('请输入单位：')
if unit == 'in' or unit == '英寸':
    print('%f英寸 = %f厘米' % (value,value * 2.54))
elif unit == 'cm' or unit == '厘米':
    print('%f厘米 = %f英寸' % (value,value / 2.54))
else:
    print('请输入有效单位')

'''成绩等级'''
"""
百分制成绩转等级制成绩
90分以上，输出A
80分~89分，输出B
70分~79分，输出C
60分~69分，输出D
60分以下，输出E
"""
score = float(input('请输入成绩:'))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('对应等级是：', grade)

'''分段函数求解'''
'''
        3x - 5 (x > 1)
f(x) =  x + 2  (-1 <= x <= 1)
        5x + 3 (x < -1)
'''
x = float(input('x = '))
if x > 1:
    y = 3 * x -5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))

'''掷色子决定做什么事情'''
face = random.randint(1, 6)
if face == 1:
    result = '唱首歌'
elif face == 2:
    result = '跳个舞'
elif face == 3:
    result = '学狗叫'
elif face == 4:
    result = '做运动'
elif face == 5:
    result = '念绕口令'
else:
    result = '讲冷笑话'
print(result)

'''报税系统'''
"""
输入月收入和五险一金计算个人所得税
说明：写这段代码时新的个人所得税计算方式还没有颁布
"""
salary = float(input('本月收入: '))
insurance = float(input('五险一金: '))
diff = salary - insurance - 3500
if diff <= 0:
    rate = 0
    deduction = 0
elif diff < 1500:
    rate = 0.03
    deduction = 0
elif diff < 4500:
    rate = 0.1
    deduction = 105
elif diff < 9000:
    rate = 0.2
    deduction = 555
elif diff < 35000:
    rate = 0.25
    deduction = 1005
elif diff < 55000:
    rate = 0.3
    deduction = 2755
elif diff < 80000:
    rate = 0.35
    deduction = 5505
else:
    rate = 0.45
    deduction = 13505
tax = abs(diff * rate - deduction)
print('个人所得税: ￥%.2f元' % tax)
print('实际到手收入: ￥%.2f元' % (diff + 3500 - tax))

'''用户身份验证'''
username = input('请输入用户名:')
password = input('请输入口令:')
if username == 'admin' and password == '123456':
    print('成功')
else:
    print('验证失败')


'''三角形验证'''
"""
判断输入的边长能否构成三角形
如果能则计算出三角形的周长和面积
"""
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('周长: %f' % (a + b + c))
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('面积: %f' % area)
else:
    print('不能构成三角形')