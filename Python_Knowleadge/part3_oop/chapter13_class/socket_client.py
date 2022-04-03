# -*- coding:utf-8 -*-
"""
DateTime    :2022/4/3 11:42:55
Author      :chuanming
File        :socket_client
Description :
*Copyright @ chuanming 2022. All rights reserved
"""

import socket 

def clientTCP():
    """socket TCP 客户端操作"""
    HOST="127.0.0.1"
    PORT=3434

    #AF_INEF说明使用IPV4地址,SOCK_STREAM指明TCP协议
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((HOST,PORT))
    print(f"连接成功{HOST}:{PORT}")
    data=s.recv(1024)              #接受数据,本次接受数据的最大长度1024
    print(f"接送数据：{data}")
    s.close()                       #关闭连接


def clientUDP():
    """socket UDP 客户端操作"""
    HOST="127.0.0.1"
    PORT=3435
    # AF_INEF说明使用IPv4地址，SOCK_DGRAM 指明 UDP
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    data="Hello UDP !"
    s.sendto(str.encode(data,"utf-8"),(HOST,PORT))
    print(f"发送{data}到{HOST}:{PORT}")
    s.close()
