# -*- coding:utf-8 -*-

"""
DateTime    :2021/8/4 21:50
Author      :chuanmingxie
File        :.py
Software    :PyCharm
Description :编码示例-你的名字
"""

def binencode():
    v1 = "谢"
    v2 = "谢".encode("utf-8")
    v3 = "谢".encode('gbk')
    name = "传明"
    # 字符串编码为二进制
    name_utf8 = name.encode(encoding='utf-8')
    print(name_utf8)
    name_gbk = name.encode(encoding='gbk')
    print(name_gbk)

    # 二进制编码为字符串
    print(name_utf8.decode(encoding='utf-8'))
    print(name_gbk.decode(encoding='gbk'))

    # 将内存文字写入文本
    text = "功高不自居，\n名高不自誉，\n位高不自傲"
    # 打开一个文件
    data = text.encode("utf-8")
    # 在文件中写内容
    file_object = open("log.txt", mode="wb") 
    # 关闭文件 file_object.close()
    file_object.write(data)

def nameencode():
    name = '云海鲸明'
    for word in name:
        word_bytes = bytes(word, encoding='utf-8')
        word_bin = ' '.join(bin(word) for word in word_bytes)
        print(word, word_bin)
