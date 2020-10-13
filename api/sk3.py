import binascii
import struct
import time
from datetime import datetime
import binascii


# 心跳包 0x2 16 0x21 AnchorHeartbeat 3 0x3
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
def zhuce():
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
    UID = binascii.unhexlify("01aa6083cf222222")
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
    Tx_Time = bytes(int(time.time()))
    CRC = 3
    ETX = 0x3
    data = struct.pack('<bhbB5shb', STX, len1, FnCE, Seq, Tx_Time, CRC, ETX)

    return data


# 在启动TDOA定位后，所有的基站都会向定位引擎发送时间同步包接收报告，即CCPRX_Report。
def CCPRX_Repor(Seq):
    STX = 0x2
    len1 = 93
    FnCE = 0x31

    Src_Addr = b'01aa6083cf920888'

    Tx_Time = bytes(int(time.time()))
    extLen = 0
    Diagnostics = b'abc'
    CRC = 3
    ETX = 0x3
    data = struct.pack('<bhbB8s5sb78shb', STX, len1, FnCE, Seq, Src_Addr[::-1], Tx_Time, extLen, Diagnostics, CRC, ETX)

    return data


# 在启动TDOA定位后，所有的定位基站会向定位引擎发送定位数据包
def BLINK_Report(Seq):
    STX = 0x2
    len1 = 114
    FnCE = 0x32
    Tag_Addr = b'01aa6083cf920000'
    Tx_Time = bytes(int(time.time()))
    extLen = 0
    Data = b'aaaasadasdasd'
    Diagnostics = b'abc'
    CRC = 3
    ETX = 0x3
    data = struct.pack('<bhbB8s5sb20s78shb', STX, len1, FnCE, Seq, Tag_Addr[::-1], Tx_Time, extLen, Data, Diagnostics,
                       CRC, ETX)

    return data
