# -*- coding:utf-8 -*-

"""
DateTime    :2021/8/4 21:50
Author      :chuanmingxie
File        :01_编码示例-你的名字.py
Software    :PyCharm
Description :
"""
name = '谢传明'

for word in name:
    word_bytes = bytes(word, encoding='utf-8')
    word_bin = ' '.join(bin(word) for word in word_bytes)
    print(word, word_bin)
