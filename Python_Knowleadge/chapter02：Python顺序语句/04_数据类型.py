# -*- coding:utf-8 -*-

"""
DateTime    :2021/8/1 18:54
Author      :chuanmingxie
File        :04_数据类型.py
Software    :PyCharm
Description :
"""

print(666)

'''整数运算'''

# 1. 加
print(1 + 2)
# 2. 减
print(3 - 1)
# 3. ×
print(3 * 10)
# 4. /
print(10 / 3)
# 5. 商
print(10 // 3)
# 6. %
print(10 % 3)
# 7. 幂
print(2 ** 10)

"""字符串运算"""
print("""
墙角数枝梅,
凌寒独自开.
遥知不是雪,
为有暗香来.
""")

print('我是chuanmingxie')
print('我是"chuanmingxie"')
print("我是'chuanmingxie'")

print('君子'+'成人之美')
print('小人常戚戚' * 3)
'''布尔类型'''
print(True)
print(False)

print(1 > 2)
print(1 == 2)
"""类型转换"""
# 1. 布尔转整形
print(True, int(True))
print(False, int(False))
# 2. 字符串转整形
print('123', int('123'))
#print('hello', int('hello'))
# 3. 整形转字符串
print(12, str(12))
# 4. 布尔转整形
print(True, str(True))
print(False, str(False))
# 5. 整形转布尔
print(12, bool(12))
print(0, bool(0))
# 6. 字符串转布尔
print('sasasa', bool('sasasa'))
print('莎莎', bool('莎莎'))
print('', bool(''))
print(bool(1))
print(bool(10))
print(bool(0))
'''变量'''
