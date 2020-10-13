# import binascii
# import ctypes
# import struct
# def aa(XYZ):
#     list1 = []
#     for i, j in zip(XYZ[::2], XYZ[1::2]):
#         list1.append(i + j)
#     k = 8
#     addr=''
#     while k > 0:
#         k -= 1
#         addr += list1[k]
#
#     return addr
#
#
# print(aa('1b978070baa803c2'))
# a='01b978070baa803c2'
# print(binascii.a2b_hex('c203a8ba7080971b'))
# b=b"\xc2\x03\xa8\xbap\x80\x97\x1b"
# c=b'\x21'
# print(binascii.b2a_hex(b))
# print(int("1b978070baa803c2", 16))
#
#
# STX = 0x2
# len1 = 63
# FnCE = 0x42
# UID = 'c203a8ba7080971b'
# UID2=int(UID, 16)
# Version = b'v888788'
# CRC = 3
# ETX = 0x3
# bytes = struct.pack('<bhb', STX, len1, FnCE)
# bt1 = struct.pack('<Q',UID2)
# # bt1=b'\xc2\x03\xa8\xbap\x80\x97\x1b'
# bt3 = struct.pack("<54s", Version)
# bt4 = struct.pack('<hb', CRC, ETX)
# bytes1 = bytes + bt1 + bt3 + bt4
#
#
# def unpack_helper(fmt, data):
#     size = struct.calcsize(fmt)
#     return struct.unpack(fmt, data[:size]), data[size:]
#
#
# def dec_hex(str1):  # 十转十六
#     a = str(hex(eval(str1)))
#     b = a.replace("0x", '')
#     print('十进制  \t%s\t十六进制\t%s' % (str1, a))
#     return b
#
#
# def hex_dec(str2):  # 十六转十
#     b = eval("0x" + str2)
#     print('---111',b)
#     # a = str(b).replace("0x", '')
#     #print('十六进制\t%s\t十进制  \t%s' % (str2, a))
#     print('十六进制\t%s\t十进制  \t%x' % (str2, b))
#
#
#
#
#
# import struct
# import ctypes
# import binascii
#
# def makePkt():
#     #例如按照tlv格式三元组的形式存储几个字段数据
#     name = (1,6,b'python')
#     nas_ident = (2,4,b'xian')
#     #创建一个内存区存储对应的数据字段
#     buffer = ctypes.create_string_buffer(128)
#     offset = 7
#     #name filed
#     fmt = struct.Struct('II6s')
#     struct.pack_into('II6s',buffer,offset,*name)
#     offset += fmt.size
#     #nas_ident
#     fmt = struct.Struct('II4s')
#     struct.pack_into('II4s',buffer,offset,*nas_ident)
#     offset += fmt.size
#     print(binascii.hexlify(buffer))
#     return binascii.hexlify(buffer) #转化成序列化编码
#
# def parsePkt(pkt):
#     unpkt = binascii.unhexlify(pkt)
#     offset = 0
#     #name
#     fmt = struct.Struct('b15s')
#     name_tag,name_len,name_value = struct.unpack_from('b15s',unpkt,offset)
#     offset += fmt.size
#     #nas_ident
#     fmt = struct.Struct('b15s')
#     nas_tag,nas_len,nas_value = struct.unpack_from('b15s',unpkt,offset)
#     offset += fmt.size
#     print(name_tag,'+',name_len,'+',name_value)
#     print(nas_tag,'+',nas_len,'+',nas_value)

# if __name__ =="__main__":
#     pkt = makePkt()
#     parsePkt(b'!AnchorHeartbeat')

# print(struct.pack('h', 63))
# a= b'\0x2'+struct.pack('h', 63)+b'\0x42'+struct.pack('8s',b'01aa6083cf920582')+struct.pack('54s', b'v888788')+struct.pack('h', 3)+b'\0x3'
# print(a)
# data=(0x2,63,0x42,b'01aa6083cf920582',b'v888788',3,0x3)
# by=struct.pack('bhb8s54shb',*data)
# print(by)



# print(hex_dec('01aa6083cf920582'))
# fmt_head="Q"
# head,probuf =  unpack_helper(fmt_head,bt1)
# print('----',bt1,head,probuf)
# print(dec_hex('13980203186993010459'))
# # print(binascii.a2b_hex('AnchorHeartbeat'))
#
# a1=b"test buf"
# leng=len(a1)
# fmt="i%ds"%leng
# buf=struct.pack(fmt,1,a1)
# print(repr(buf))


STX = 0x2
len1 = 63
FnCE = 0x42
UID = b'01aa6083cf920582'
# print(int(UID, 16))
UID2=int(UID, 16)
Version = b'v888788'
CRC = 322
ETX = 0x3
s=bytearray

print(s)
data=(0x2,63,0x42,UID,b'v888788',3,0x3)
a=bytes.fromhex('01aa6083cf920582')
b=('v888788')
print(a,b,bytes(0x3),hex(63))

b=b'C\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00D"\x02\t\x14\x00'

print(b.hex().encode(encoding="utf-8"))



