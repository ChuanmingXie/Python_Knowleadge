# -*- coding:utf-8 -*-

"""
DateTime    :2021/8/4 21:55
Author      :chuanmingxie
File        :04_基础小结.py
Software    :PyCharm
Description :
"""

name = "生活不是电影,生活比电影沉重"
print(name[8:1:-1])  # 从第9位倒序到都二位 ‘活生,影电是不’
print(name[-1:1:-1])  # 从最后一位倒序到第二位 ’重沉影电比活生,影电是不‘
print(name[-1::-1])  # 从最后一位倒叙到第一位 ’重沉影电比活生,影电是不活生‘

# 1.代码实现进制转换
v1 = 675  # 转化为2进制
print(bin(v1))
v2 = "0b11000101"  # 转化为十进制
print(int(v2, base=2))
v3 = "11000101"  # 转化为十进制
print(int(v3, base=2))

# 2. 现有v1=123和v2=456.请将这两个值转化为二进制，并将0b字符去除，链接两二进制数后再次转化为十进制
v1 = 123
v2 = 456
# vBin1 = bin(v1)
# vBin2 = bin(v2)
# data = vBin1[2:] + vBin2[2:]
data = bin(v1)[2:] + bin(v2)[2:]
result = int(data, base=2)
print(result)

# 3.对上提的二进制补齐0后再次拼接转换
vv1 = 123
vv2 = 456
data2 = bin(vv1)[2:].zfill(16) + bin(vv2)[2:].zfill(16)
print(int(data2, base=2))

# 那些数据类型转换为布尔类型时为False
"""
空类型、0 两者转换为布尔值时为False
"""

# 屏蔽敏感词，将文本中的’最有效‘、’立马见效‘等 替换为’***‘
text = input('请输入内容:')
text = text.replace('最有效', '***')
text = text.replace('立马见效', '***')

# 实现字符串反转
name = "上官秦风"
data = name[::-1]
print(data)

# 现有字符串 s='123a456c',请测试切片方法
s = '123a456c'
print(s[0:3])
print(s[3:6])
print(s[-1])
print(s[len(s) - 1])
print(s[-3:0:-2])

# while+索引 数组输出
message = '转轴拨弦三两声，未成曲调先有请'
index = 0
while index < len(message):
    print(message[index])
    index += 1

# for 循环 数据输出

# for 循环＋range+索引

# 使用for循环实现输出倒计时效果，例如：输出内容依次是："倒计时3秒"，"倒计时2秒"，

# 让用户输入一段文本，请计算文本中 "浪" 出现的次数，并输入结果

# 获取用户两次输入的内容，并提取其中的数字，然后实现数字的相加（转换为整型再相加）
