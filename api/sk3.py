import binascii
import math
import struct
import time
from datetime import datetime
import binascii


# 心跳包 0x2 16 0x21 AnchorHeartbeat 3 0x3
from cou import sqr


def xintiao():
    STX = 0x2
    len1 = 16
    FnCE = 0x21
    UID = b"AnchorHeartbeat"
    CRC = 3
    ETX = 0x3
    fmt = "<15s"
    bt = struct.pack(fmt, UID)
    bytes = struct.pack('<bhb', STX, len1, FnCE)
    bt2 = struct.pack('<hb', CRC, ETX)
    bytes2 = bytes + bt + bt2
    return bytes2


# 注册数据包  0x2130x42ffffffffv66630x3
def zhuce(addr):
    # STX = 0x2
    # len1 = hex(63)
    # FnCE = 0x42
    # UID = int.from_bytes(b'01aa6083cf920582', 'big')
    # UID2 = bytes.fromhex('01aa6083cf920582')
    # Version = b'v888788'
    # CRC = 322
    # ETX = 0x3
    # data = (STX, len1, FnCE, UID, Version, CRC, ETX)
    # by = struct.pack('=b2cbd54shb', *data)
    STX = struct.pack('=B', int('0x2', 16))
    len1 = struct.pack('h', 64)
    FnCE = struct.pack('=B', int('0x42', 16))
    UID = binascii.unhexlify(addr)
    Comm_Type = struct.pack('=b', 5)
    Version = struct.pack('54s', b'v888788')
    CRC = struct.pack('h', 63)
    ETX = struct.pack('=B', int('0x3', 16))
    data = STX + len1 + FnCE + UID[::-1] + Comm_Type + Version + CRC + ETX

    return data


# 在启动TDOA定位后，所有的时间同步参考基站都会向定位引擎发送时间同步包发送报告

def CCPTX_Report(Seq):
    STX = 0x2
    len1 = 7
    FnCE = 0x30
    time = 111131111111
    b = struct.pack('q', time)
    Tx_Time = b[0:5]

    CRC = 3
    ETX = 0x3
    data1 = struct.pack('<bhbB', STX, len1, FnCE, Seq)+ Tx_Time
    data2=struct.pack('hb',CRC, ETX)
    return data1+data2

# 在启动TDOA定位后，所有的基站都会向定位引擎发送时间同步包接收报告，即CCPRX_Report。
def CCPRX_Report(Seq,time,addr):
    STX = 0x2
    len1 = 18
    FnCE = 0x31
    Src_Addr=binascii.unhexlify(addr)
    # time = time +sqr( math.sqrt(2)*200)
    b = struct.pack('Q', time)
    Tx_Time = b[0:5]
    # print('次基站CCPRX_Report时间戳',Tx_Time,'FnCE:',struct.pack('b',FnCE))
    LL = 0
    extLen = 0
    CRC = 3
    ETX = 0x3
    data1 = struct.pack('<bhbB', STX, len1, FnCE, Seq)+Src_Addr[::-1]+ Tx_Time
    data2 = struct.pack('<hbhb',LL,extLen, CRC, ETX)
    # print('原始报文 STX+len1+FnCE+Seq+Src_Addr+time+LL+extLen+CRC+ETX：',STX,len1,FnCE,Seq,'01aa6083cf111111',time,LL,extLen,CRC,ETX)
    # print(data1+data2)
    return data1+data2

# 在启动TDOA定位后，所有的定位基站会向定位引擎发送定位数据包
# 在启动TDOA定位后，所有的定位基站会向定位引擎发送定位数据包
def BLINK_Report(Seq,Tag_Addr,time):

    STX = 0x2
    len1 = 18
    FnCE =0x32
    # time = 10000 +sqr( math.sqrt(2)*200)+sqr(math.sqrt(2)*100)
    # Seq=struct.pack('B', Seq)
    # Tag_Addr = b'cf9aaaaa'
    b = struct.pack('q', time)
    Tx_Time = b[0:5]
    LL = 0
    extLen = 0
    Diagnostics = b'abcde'
    Tag_Addr2=binascii.unhexlify(Tag_Addr)

    CRC = 3
    ETX = 0x3
    data1 = struct.pack('<bhbB', STX, len1,FnCE, Seq)+ Tag_Addr2[::-1]+ Tx_Time
    data2 = struct.pack('<hbhb',LL,extLen, CRC, ETX)
    return data1+data2
