import random
import os
import json
from imp import reload

# import unit
#
# filename = unit.BASE_DIR + "\data\Bilk_data.json"
# json2 = unit.read_name_data(filename, "Blik_time")
#
# #
# # # 函数调用
# filename = unit.os.path.dirname(os.path.abspath(__file__)) +  "\data\Bilk_data.json"
#
# file_new=os.path.dirname(os.path.abspath(__file__)) + "\\data\\xyz1.json"
# with open(filename, 'r') as f:
#     data = json.load(f)
    # data[0]['a'] = 'rect'

import xlsxwriter
import datetime
import time

#startTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')#现在
#print startTime
startTime1 = time.time()
#print startTime1

workbook = xlsxwriter.Workbook('d:\kami1.xlsx')  #创建一个Excel文件
worksheet = workbook.add_worksheet()               #创建一个sheet

title = [U'名称',U'副标题']     #表格title
worksheet.write_row('A1',title)                    #title 写入Excel

for i in range(1,5):
    num0 = i+5
    num = i
    row = 'A{}'.format(num0)
    data = [u'学生'+"11",num,]
    worksheet.write_row(row, data)
    i+=1

workbook.close()

ipTable = ['158.59.194.213', '18.9.14.13', '58.59.14.21']
fileObject = open('sampleList.txt', 'w')
for ip in ipTable:
    fileObject.write(ip)
    fileObject.write('\n')
fileObject.close()