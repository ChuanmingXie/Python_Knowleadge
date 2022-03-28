# -*- coding:utf-8 -*-

"""
DateTime    :2021/8/4 21:54
Author      :chuanmingxie
File        :02_字符串.py
Software    :PyCharm
Description :
"""
# 1.字符串的定义
str1 = '人生只管努力，其他交给天意'
str2 = "人生只管努力，其他交给天意"
str3 = '''人生只管努力，其他交给天意'''
str4 = """人生只管努力，其他交给天意"""
str5 = '人生不得已，自己当"主角"'
str6 = "人生不得已，自己当'主角'"

# 2. 字符串开始与结尾
str7 = '孟子曰：爱人者，仁恒爱之；敬人者，人恒敬之'
print(str7.startswith('孟子曰'))
print(str7.endswith('之'))




#字符按串切片
str = 'chuanmingxie'

print (str)          # 输出字符串
print (str[0:-1])    # 输出第一个到倒数第二个的所有字符
print (str[0])       # 输出字符串第一个字符
print (str[2:5])     # 输出从第三个开始到第五个的字符
print (str[2:])      # 输出从第三个开始的后的所有字符
print (str * 2)      # 输出字符串两次，也可以写成 print (2 * str)
print (str + "TEST")  # 连接字符串


