import time
import socket
import struct
from datetime import datetime

import unit
from script.xintiao import sk3

sk1=sk3

if unit.server_state == -10:
    # 基站信息包
    # 字段  STX  len1  FnCE  UID      Version  CRC  ETX
    # 长度  1    2     1     8        4        2    1
    #  值  0x2  13    0x42  12345678 v666      3    0x3
    STX = 0x2
    len1 = 13
    FnCE = 0x42
    UID = b'88888888'
    Version = b'v666'
    CRC = 3
    ETX = 0x3
    q = struct.pack('<h', len1)
    bytes = struct.pack('<bhb', STX, len1, FnCE)
    bt1 = struct.pack('<8s', UID)
    print(len(q), len(bt1))
    bt3 = struct.pack("<4s", Version)
    print(len(bt3))
    bt4 = struct.pack('<hb', CRC, ETX)
    bytes1 = bytes + bt1 + bt3 + bt4
    print(len(bytes1))
    sk1.send(bytes1)
    while True:
        msg = sk1.recv(1024)
        if msg!=b'':
            print(msg)
            print("基站信息包：", datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3], "\n\t", bytes1)
            print("服务器：", msg)


else:
    print("服务器连接失败：请检查网络连接或者服务端是否启动！状态码：-1")
