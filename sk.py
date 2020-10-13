import struct

from script.xintiao import zhuce
# 基站信息包
    # 字段  STX  len1  FnCE  UID      Version  CRC  ETX
    # 长度  1    2     1     8        4        2    1
    #  值  0x2  13    0x42  12345678 v666      3    0x3
STX = 0x2
len1 = 13
FnCE = 0x42
UID = b'c203a8ba7080971b'
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
zhuce(bytes1)