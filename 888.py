# # # -*- coding: cp936 -*-
# # import struct  # 16进制转换浮点型
# # import os
# # import sys
# # import xlwt
# # import xlrd
# #
# #
# # # from xlrd import *
# #
# # def learn_to_pack_func():
# #     ''
# #     while (1):
# #         op_id = int(raw_input('please select float to hex(0) or hex to float(1),other value to quit:'))
# #         if op_id == 0:
# #             num = float(raw_input('please input the float number:'))
# #             result = struct.pack('>f', num).encode('hex')
# #             print
# #             result
# #         elif op_id == 1:
# #             num = str(raw_input('please input the hex number:'))
# #             str1 = num[2:]
# #             str2 = struct.unpack('>f', (str1.decode('hex')))
# #             print
# #             str2
# #         else:
# #             break
# #     return 0
# #
# #
# # def read_data_from_excel(filePath, readData):
# #     ''
# #     # read data from excel
# #     bk = xlrd.open_workbook(filePath)
# #     shxrange = range(bk.nsheets)
# #     try:
# #         sh = bk.sheet_by_name('Sheet1')
# #     except:
# #         print
# #         "no sheet in %s named Sheet1" % fname
# #     # 获取行数
# #     nrows = sh.nrows
# #     # 获取列数
# #     ncols = sh.ncols
# #     # 获取数据
# #     for i in range(0, nrows):
# #         for j in range(0, ncols):
# #             readData.append(sh.cell(i, j).value)
# #     return 0
# #
# #
# # def save_data_to_excel(filePath, writeData):
# #     ''
# #     bk = xlwt.Workbook(encoding='utf-8')
# #     ws = bk.add_sheet('Sheet1', cell_overwrite_ok=False)
# #
# #     for i, row in enumerate(writeData):
# #         for j, clo in enumerate(row):
# #             ws.write(i, j, clo)
# #     bk.save(filePath)
# #
# #
# # def LEEE754Data_Hex_To_Float_Translate():
# #     ''
# #     cwd = os.getcwd()
# #     path = cwd + '\data.xls'
# #     path_1 = cwd + '\data_1.xls'
# #     Data_Source = []
# #     Data_Result = []
# #     # 获取数据
# #     read_data_from_excel(path, Data_Source)
# #     # 数据转换
# #     for i in range(len(Data_Source)):
# #         num = Data_Source[i]
# #         str1 = num[2:]
# #         str2 = struct.unpack('>f', (str1.decode('hex')))
# #         Data_Result.append(str2)
# #     # 保存数据
# #     save_data_to_excel(path_1, Data_Result)
# #     return 0
# #
# #
# # def main():
# #     ''
# #     op_mode = int(raw_input('please select opreation mode(0:auto,1:manual):'))
# #     if 0 == op_mode:
# #         LEEE754Data_Hex_To_Float_Translate()
# #     elif 1 == op_mode:
# #         learn_to_pack_func()
# #     else:
# #         print('error')
# #
# #
# # if __name__ == '__main__':
# #     main()
# #
# # def fix2float(v, s=False, w=24, f=15):
# #     # v 输入16进制字符串 example 'f1'
# #     # s 是否是有符号输出 example  1
# #     # w 输入值位宽      example  8
# #     # f 小数位宽        example  4
# #     # return           -0.9375
# #     din = int(v, 16)
# #     max_num = 2 ** w
# #
# #     if (s and din >= max_num / 2):
# #         x = din ^ (max_num - 1)
# #         v_bin = '{0:0{1}b}'.format(x + 1, w)
# #         fraction = int(v_bin[w - f:], 2) / float(2 ** f)
# #         intdata = int(v_bin[:w - f], 2)
# #         x = -(fraction + intdata)
# #     else:
# #         v_bin = '{0:0{1}b}'.format(din, w)
# #         fraction = int(v_bin[w - f:], 2) / float(2 ** f)
# #         intdata = int(v_bin[:w - f], 2)
# #         x = fraction + intdata
# #     return x
# # b='65 59ddfd4d1337f73f abd6fbc461281140 0000000000000000 1ec032cd0001cade'
# # a=' E162606DC362FB3F EAE4C6FEE32C1140  0000000000000000'
# # c='4145B4A2'
# # print(fix2float(c))
# # # print(a.encode('utf-8', 'strict'))
# #
# import ctypes
# import struct
#
# x="1112adiuhik"
# a=1
# for i in x:
#     if i=="q":
#         a=0
#
# print(a)
# if a==1:
#     print("吃饭")
# a=1.6224
# # print(hex(a))
# print(int("3FF8C410E570B22F",16))
# print(int("2fb270e510c4f83F",16))
# from ctypes import *
# def double_to_hex(f):
#     return hex(struct.unpack('<Q', struct.pack('<d', f))[0])
#
# # code = code.decode('utf-8')
# print(double_to_hex(1.5861))
# b=str(struct.pack("<f", 1.5861))
#
# # str=str(5464).encode("utf-8").decode('hex')
# # print(str)
#
# def h2f(s):
#     cp = ctypes.pointer(ctypes.c_longlong(s))
#     fp = ctypes.cast(cp, ctypes.POINTER(ctypes.c_double))
#     return fp.contents.value
# def f2h(s):
#     fp = ctypes.pointer(ctypes.c_double(s))
#     cp = ctypes.cast(fp, ctypes.POINTER(ctypes.c_longlong))
#     return hex(cp.contents.value)
# print(f2h(41.5861))
# print(h2f(0x3FF8C410E570B22F))
# print(h2f(0x3410fc18795ef93f))
# print(type(88))
# # "1.5856 4.3831  1.6055 4.3463 1.6070 4.3494"
# x="b'653410fc18795ef93f801ef4f36a80114000000000000000001ec032cd0001cade'"
# # b'65a0e2056b308ef93f128bf5029479114000000000000000001ec032cd0001cade'
# # b'65 da23e4b4beaff93f 727de81a8a741140 0000000000000000 1ec032cd0001cade'
# dat=x.split("'",1)
# dat_X=dat[1][2:18]
#
# dat_Y=dat[1][18:34]
# dat_Z=dat[1][34:50]
# dat_adr=dat[1][50:66]
# aa='0x'+dat_X
# print(aa)
# print(dat_X,"是我")
# print(dat_X[::-2],"是我")
# print(dat_X[::-2],"是我")
# print(dat_Y)
# print(dat_Z)
# print(dat_adr)
# print(h2f(int(dat_Z)))
# assa=int(dat_X,16)
# print(assa)
# print(h2f(assa))
#
# print(dat_X)
# list1=[]
# cou=0
# for i, j in zip(dat_X[::2], dat_X[1::2]):
#   print (i+j)
#   list1.append(i+j)
# print(list1)
# k=8
# addr='0X'
# while k>0:
#     k-=1
#     addr+=list1[k]
# print(addr)
# print('%.4f' %h2f(int(addr,16)))
# import requests
# requests.get("10.14.1.88:59334")

a=0
x=2
while a<21:
    x*=2

    a+=1
print(x)
import time
import datetime
print(int(time.time()))
a=int(time.time())
a=1899854235
print(datetime.datetime.utcfromtimestamp(a))