# -*- coding:utf-8 -*-
"""
DateTime    :2022/4/3 11:53:36
Author      :chuanming
File        :socket_server
Description :
*Copyright @ chuanming 2022. All rights reserved
"""

import socket
import datetime

def serverTCP():
    """socket TCP 服务端操作"""
    HOST='0.0.0.0'
    PORT=3434

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((HOST,PORT))     # 绑定IP和端口
    s.listen(1)             # 监听

    while True:
        conn,addr=s.accept()                   # 接受TCP链接，并返回新的Socket对象
        print(f"客户端：{str(addr)}已连接")    # 输出客户端的IP地址
        dt=datetime.datetime.now()
        message="Current time is "+str(dt)
        #conn.send(bytes(message,encoding='utf-8')) #错误，向客户端发送当前时间
        #conn.send(message.encode('utf-8'))         #错误，向客户端发送当前时间
        conn.send(str.encode(message,'utf-8'))      #向客户端发送当前时间
        print(f"发送消息：{message}")
        conn.close()                    #关闭链接

def serverUDP():
    """socket UDP 服务端操作"""
    HOST="0.0.0.0"
    PORT=3435
    # AF_INEF说明使用IPv4地址，SOCK_DGRAM 指明 UDP
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind((HOST,PORT))
    
    while True:
        data,addr=s.recvfrom(1024)
        print(f"接受{data}来自{str(addr)}")
    s.close()
