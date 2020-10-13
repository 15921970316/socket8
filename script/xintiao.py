# 客户端
import time
import socket
import struct
from datetime import datetime


class sket():
    def setUpClass(cls):
        print('开始连接')
        cls.sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cls.sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        cls.sk.bind(('10.10.90.17', 19970))  # 自己的端口号设置
        cls.sk.connect(('10.14.1.88', 59336))  # 链接到服务器端 括号里也是一个元组，包含ip地址以及服务器的端口号

    def tearDownClass(cls):
        cls.sk.close()
        print('关闭连接')

    # 心跳包：
    def xintiao(cls):
        STX = 0x2
        len = 16
        FnCE = 0x21
        UID = b"AnchorHeartbeat"
        CRC = 3
        ETX = 0x3
        fmt = "<15s"
        bt = struct.pack(fmt, UID)
        bytes = struct.pack('<bhb', STX, len, FnCE)
        bt2 = struct.pack('<hb', CRC, ETX)
        bytes2 = bytes + bt + bt2
        cls.sk.send(bytes2)
        # 收发信息也需要循环
        # while True:
        #     # 心跳间隔是2秒 2秒发送一个心跳包并且收到引擎一个心跳回访 一旦超时未收到双方连接立即中断
        #     time.sleep(2)
        cls.sk.send(bytes2)

        try:  # 为了防止服务器非正常下线而导致客户端直接崩溃，需要加入异常处理
            msg = cls.sk.recv(1024)
            print("基站心跳包：", datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3], "\n\t", bytes2)
            print("服务器：", str(msg, 'utf8'))
        except Exception as e:
            print(e, 1111)
            # break

    # 注册数据包  0x2130x42
    def zhuce(cls):
        STX = 0x2
        len1 = 13
        FnCE = 0x42
        UID = b'0000.!2#'
        Version = b'v666'
        CRC = 3
        ETX = 0x3
        bytes = struct.pack('<bhb', STX, len1, FnCE)
        bt1 = struct.pack('<8s', UID)
        bt3 = struct.pack("<4s", Version)
        bt4 = struct.pack('<hb', CRC, ETX)
        bytes1 = bytes + bt1 + bt3 + bt4
        cls.sk.send(bytes1)
        msg = cls.sk.recv(1024)
        print("基站信息包：", datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3], "\n\t", bytes1)
        print("服务器：", msg)

xintiao()
zhuce()
