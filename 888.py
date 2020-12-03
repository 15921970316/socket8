# # # # # import binascii
# # # # # import ctypes
# # # # # import struct
# # # # # # t1= int(round(time.time()*1000))
# # # # # # s=int(time.time())
# # # # # # # print(struct.pack('<5s',bytes(t)))
# # # # #
# # # # # # print(s)
# # # # # # STX = 0x2
# # # # # # len1 = 7
# # # # # # FnCE = 0x30
# # # # # # Seq=0
# # # # # # Tx_Time =str(int(round(t * 1000000000000000000000000000000))).encode('utf-8')
# # # # # # CRC = 3
# # # # # # ETX = 0x3
# # # # # # print(Tx_Time)
# # # # # # data = struct.pack('<bhbB5shb', STX, len1, FnCE, Seq, Tx_Time, CRC, ETX)
# # # # # # print(data)
# # # # #
# # # # # t = time.time()#时间戳
# # # # # #
# # # # # print (t)                       #原始时间数据
# # # # # print (int(t))                  #秒级时间戳
# # # # # print (int(round(t * 1000)))    #毫秒级时间戳
# # # # # print (int(round(t * 1000000))) #微秒级时间戳
# # # # # a=int(round(t * 1000000000000000000000000000000))
# # # # # print(a)
# # # # #
# # # # # print(len(str(int(round(t * 1000000000000000000000000000000)))))
# # # # #
# # # # # print(struct.pack('q', int(round(t * 1000000))))
# # # # # # a1=16026660
# # # # # # a2=77751308
# # # # # # a3=93109703
# # # # # # a4=75122160
# # # # # # a5=30478336
# # # # # # print(len(bin(a)))
# # # # # # print(a)
# # # # import json
# # # # import math
# # # # # import struct
# # # # # import time
# # # # #
# # # # # import unit
# # # # #
# # # # # a = 11111
# # # # #
# # # # # x = b'[]'
# # # # # b = struct.pack('q', a)
# # # # #
# # # # # print(b)
# # # # # print(b'111' + b'0')
# # # # #
# # # # # filename = unit.BASE_DIR + "\data\Bilk_data.json"
# # # # # json1 = unit.read_name_data(filename, "Tag_Addr")
# # # # # print(json1[0][100])
# # # # # a = 0
# # # # # b = '11111111'
# # # # # i = 0
# # # # # # while i < 201:
# # # # # #     print('"{}":b"{}"'.format(a, b)+',')
# # # # # #     a += 1
# # # # # #     b += 1
# # # # # #     i += 1
# # # # # print(int(json1[0][100],16))
# # # # # print(b.encode('utf-8'))
# # # # # print(bytearray("1111asd",encoding='utf-8'))
# # # # # Seq = 0
# # # # # while True:
# # # # #     try:
# # # # #         if Seq == 255:
# # # # #             Seq = 0
# # # # #         for k in range(0, 200, 1):
# # # # #             print('---------1', Seq)
# # # # #
# # # # #         Seq += 1
# # # # #     except    Exception as e:
# # # # #         # print('服务器连接失败--3', e)
# # # # #         ...
# # # # #
# # # # # x=20000.0
# # # # # m=math.sqrt(x)
# # # # # t=m/299702547
# # # # # a=int(round(time.time() * 1000000000000000000000000000000))
# # # # # print(time.time() * 1000000000000000000000000000000)
# # # # # print(t,t+time.time()* 1000000000000000000000000000000)
# # # # # # b = struct.pack('q', t)
# # # # # # print(b)
# # # # # #
# # # # #
# # # # # x='aaaaaaaaaaaaa'
# # # # # j=100
# # # # # for i in range(200):
# # # # #
# # # # #     print('"{}":"{}{}",'.format(i,x,j))
# # # # #     j+=1
# # # # import struct
# # # # import time
# # # #
# # # # import cou
# # # # import unit
# # # #
# # # # # filename = unit.BASE_DIR + "\data\Bilk_data.json"
# # # # # json1 = unit.read_name_data(filename, "Tag_Addr")
# # # # # for i in json1[0]:
# # # # #     print(i)
# # # # # a=100
# # # # # for i in range(200):
# # # # #     print('"{}":"aaaaaaaaaaaaa{}",'.format(i,a+i))
# # # # # filename = unit.BASE_DIR + "\data\Bilk_data.json"
# # # # #
# # # # # json2 = unit.read_name_data(filename, "Blik_time")
# # # # # print(json2[0][0])
# # # #
# # # # # "11":"aaaaaaaaaaaaa111",
# # # "12":"aaaaaaaaaaaaa112",
# # # "13":"aaaaaaaaaaaaa113",
# # # "14":"aaaaaaaaaaaaa114",
# # # "15":"aaaaaaaaaaaaa115",
# # # "16":"aaaaaaaaaaaaa116",
# # # "17":"aaaaaaaaaaaaa117",
# # # "18":"aaaaaaaaaaaaa118",
# # # "19":"aaaaaaaaaaaaa119",
# # # "20":"aaaaaaaaaaaaa120",
# # # "21":"aaaaaaaaaaaaa121",
# # # "22":"aaaaaaaaaaaaa122",
# # # "23":"aaaaaaaaaaaaa123",
# # # "24":"aaaaaaaaaaaaa124",
# # # "25":"aaaaaaaaaaaaa125",
# # # "26":"aaaaaaaaaaaaa126",
# # # "27":"aaaaaaaaaaaaa127",
# # # "28":"aaaaaaaaaaaaa128",
# # # "29":"aaaaaaaaaaaaa129",
# # # "30":"aaaaaaaaaaaaa130",
# # # "31":"aaaaaaaaaaaaa131",
# # # "32":"aaaaaaaaaaaaa132",
# # # "33":"aaaaaaaaaaaaa133",
# # # "34":"aaaaaaaaaaaaa134",
# # # "35":"aaaaaaaaaaaaa135",
# # # "36":"aaaaaaaaaaaaa136",
# # # "37":"aaaaaaaaaaaaa137",
# # # "38":"aaaaaaaaaaaaa138",
# # # "39":"aaaaaaaaaaaaa139",
# # # "40":"aaaaaaaaaaaaa140",
# # # "41":"aaaaaaaaaaaaa141",
# # # "42":"aaaaaaaaaaaaa142",
# # # "43":"aaaaaaaaaaaaa143",
# # # "44":"aaaaaaaaaaaaa144",
# # # "45":"aaaaaaaaaaaaa145",
# # # "46":"aaaaaaaaaaaaa146",
# # # "47":"aaaaaaaaaaaaa147",
# # # "48":"aaaaaaaaaaaaa148",
# # # "49":"aaaaaaaaaaaaa149",
# # # "50":"aaaaaaaaaaaaa150"
# # # "51":"aaaaaaaaaaaaa151",
# # # "52":"aaaaaaaaaaaaa152",
# # # "53":"aaaaaaaaaaaaa153",
# # # "54":"aaaaaaaaaaaaa154",
# # # "55":"aaaaaaaaaaaaa155",
# # # "56":"aaaaaaaaaaaaa156",
# # # "57":"aaaaaaaaaaaaa157",
# # # "58":"aaaaaaaaaaaaa158",
# # # "59":"aaaaaaaaaaaaa159",
# # # "60":"aaaaaaaaaaaaa160",
# # # "61":"aaaaaaaaaaaaa161",
# # # "62":"aaaaaaaaaaaaa162",
# # # "63":"aaaaaaaaaaaaa163",
# # # "64":"aaaaaaaaaaaaa164",
# # # "65":"aaaaaaaaaaaaa165",
# # # "66":"aaaaaaaaaaaaa166",
# # # "67":"aaaaaaaaaaaaa167",
# # # "68":"aaaaaaaaaaaaa168",
# # # "69":"aaaaaaaaaaaaa169",
# # # "70":"aaaaaaaaaaaaa170",
# # # "71":"aaaaaaaaaaaaa171",
# # # "72":"aaaaaaaaaaaaa172",
# # # "73":"aaaaaaaaaaaaa173",
# # # "74":"aaaaaaaaaaaaa174",
# # # "75":"aaaaaaaaaaaaa175",
# # # "76":"aaaaaaaaaaaaa176",
# # # "77":"aaaaaaaaaaaaa177",
# # # "78":"aaaaaaaaaaaaa178",
# # # "79":"aaaaaaaaaaaaa179",
# # # "80":"aaaaaaaaaaaaa180",
# # # "81":"aaaaaaaaaaaaa181",
# # # "82":"aaaaaaaaaaaaa182",
# # # "83":"aaaaaaaaaaaaa183",
# # # "84":"aaaaaaaaaaaaa184",
# # # "85":"aaaaaaaaaaaaa185",
# # # "86":"aaaaaaaaaaaaa186",
# # # "87":"aaaaaaaaaaaaa187",
# # # "88":"aaaaaaaaaaaaa188",
# # # "89":"aaaaaaaaaaaaa189",
# # # "90":"aaaaaaaaaaaaa190",
# # # "91":"aaaaaaaaaaaaa191",
# # # "92":"aaaaaaaaaaaaa192",
# # # "93":"aaaaaaaaaaaaa193",
# # # "94":"aaaaaaaaaaaaa194",
# # # "95":"aaaaaaaaaaaaa195",
# # # "96":"aaaaaaaaaaaaa196",
# # # "97":"aaaaaaaaaaaaa197",
# # # "98":"aaaaaaaaaaaaa198",
# # # "99":"aaaaaaaaaaaaa199",
# # # "100":"aaaaaaaaaaaaa200",
# # # "101":"aaaaaaaaaaaaa201",
# # # "102":"aaaaaaaaaaaaa202",
# # # "103":"aaaaaaaaaaaaa203",
# # # "104":"aaaaaaaaaaaaa204",
# # # "105":"aaaaaaaaaaaaa205",
# # # "106":"aaaaaaaaaaaaa206",
# # # "107":"aaaaaaaaaaaaa207",
# # # "108":"aaaaaaaaaaaaa208",
# # # "109":"aaaaaaaaaaaaa209",
# # # "110":"aaaaaaaaaaaaa210",
# # # "111":"aaaaaaaaaaaaa211",
# # # "112":"aaaaaaaaaaaaa212",
# # # "113":"aaaaaaaaaaaaa213",
# # # "114":"aaaaaaaaaaaaa214",
# # # "115":"aaaaaaaaaaaaa215",
# # # "116":"aaaaaaaaaaaaa216",
# # # "117":"aaaaaaaaaaaaa217",
# # # "118":"aaaaaaaaaaaaa218",
# # # "119":"aaaaaaaaaaaaa219",
# # # "120":"aaaaaaaaaaaaa220",
# # # "121":"aaaaaaaaaaaaa221",
# # # "122":"aaaaaaaaaaaaa222",
# # # "123":"aaaaaaaaaaaaa223",
# # # "124":"aaaaaaaaaaaaa224",
# # # "125":"aaaaaaaaaaaaa225",
# # # "126":"aaaaaaaaaaaaa226",
# # # "127":"aaaaaaaaaaaaa227",
# # # "128":"aaaaaaaaaaaaa228",
# # # "129":"aaaaaaaaaaaaa229",
# # # "130":"aaaaaaaaaaaaa230",
# # # "131":"aaaaaaaaaaaaa231",
# # # "132":"aaaaaaaaaaaaa232",
# # # "133":"aaaaaaaaaaaaa233",
# # # "134":"aaaaaaaaaaaaa234",
# # # "135":"aaaaaaaaaaaaa235",
# # # "136":"aaaaaaaaaaaaa236",
# # # "137":"aaaaaaaaaaaaa237",
# # # "138":"aaaaaaaaaaaaa238",
# # # "139":"aaaaaaaaaaaaa239",
# # # "140":"aaaaaaaaaaaaa240",
# # # "141":"aaaaaaaaaaaaa241",
# # # "142":"aaaaaaaaaaaaa242",
# # # "143":"aaaaaaaaaaaaa243",
# # # "144":"aaaaaaaaaaaaa244",
# # # "145":"aaaaaaaaaaaaa245",
# # # "146":"aaaaaaaaaaaaa246",
# # # "147":"aaaaaaaaaaaaa247",
# # # "148":"aaaaaaaaaaaaa248",
# # # "149":"aaaaaaaaaaaaa249",
# # # "150":"aaaaaaaaaaaaa250",
# # # "151":"aaaaaaaaaaaaa251",
# # # "152":"aaaaaaaaaaaaa252",
# # # "153":"aaaaaaaaaaaaa253",
# # # "154":"aaaaaaaaaaaaa254",
# # # "155":"aaaaaaaaaaaaa255",
# # # "156":"aaaaaaaaaaaaa256",
# # # "157":"aaaaaaaaaaaaa257",
# # # "158":"aaaaaaaaaaaaa258",
# # # "159":"aaaaaaaaaaaaa259",
# # # "160":"aaaaaaaaaaaaa260",
# # # "161":"aaaaaaaaaaaaa261",
# # # "162":"aaaaaaaaaaaaa262",
# # # "163":"aaaaaaaaaaaaa263",
# # # "164":"aaaaaaaaaaaaa264",
# # # "165":"aaaaaaaaaaaaa265",
# # # "166":"aaaaaaaaaaaaa266",
# # # "167":"aaaaaaaaaaaaa267",
# # # "168":"aaaaaaaaaaaaa268",
# # # "169":"aaaaaaaaaaaaa269",
# # # "170":"aaaaaaaaaaaaa270",
# # # "171":"aaaaaaaaaaaaa271",
# # # "172":"aaaaaaaaaaaaa272",
# # # "173":"aaaaaaaaaaaaa273",
# # # "174":"aaaaaaaaaaaaa274",
# # # "175":"aaaaaaaaaaaaa275",
# # # "176":"aaaaaaaaaaaaa276",
# # # "177":"aaaaaaaaaaaaa277",
# # # "178":"aaaaaaaaaaaaa278",
# # # "179":"aaaaaaaaaaaaa279",
# # # "180":"aaaaaaaaaaaaa280",
# # # "181":"aaaaaaaaaaaaa281",
# # # "182":"aaaaaaaaaaaaa282",
# # # "183":"aaaaaaaaaaaaa283",
# # # "184":"aaaaaaaaaaaaa284",
# # # "185":"aaaaaaaaaaaaa285",
# # # "186":"aaaaaaaaaaaaa286",
# # # "187":"aaaaaaaaaaaaa287",
# # # "188":"aaaaaaaaaaaaa288",
# # # "189":"aaaaaaaaaaaaa289",
# # # "190":"aaaaaaaaaaaaa290",
# # # "191":"aaaaaaaaaaaaa291",
# # # "192":"aaaaaaaaaaaaa292",
# # # "193":"aaaaaaaaaaaaa293",
# # # "194":"aaaaaaaaaaaaa294",
# # # "195":"aaaaaaaaaaaaa295",
# # # "196":"aaaaaaaaaaaaa296",
# # # "197":"aaaaaaaaaaaaa297",
# # # "198":"aaaaaaaaaaaaa298",
# # # "199":"aaaaaaaaaaaaa299"
# # # #
# # # # #
# # # # # x=0x10000000000  * 1.0/499.2e6/128.0
# # # # # y= 0.1 / 499.2e6 /128.0
# # # # # z=200
# # # # # print(x,y,math.sqrt(2)*200)
# # # # # global a1
# # # # #
# # # # # def aa():
# # # # #     a1=100
# # # # #     print(a1)
# # # # # aa()
# # # # # print(a1)
# # # # t = 100005555
# # # # if len(str(t)) > 12:
# # # #     t = 10000
# # # #
# # # # # print(t, 499.2e6 * 128.0)/
# # # #
# # # # # t3 = int(0.15 * 499.2e6 * 128.0)
# # # # # while True:
# # # # #     try:
# # # # #         if t3 > 10000000000:
# # # # #             t3 = int(0.15 * 499.2e6 * 128.0)
# # # # #         d = 200 / 299702547
# # # # #         x = d * 499.2e6 * 128.0
# # # # #         t3 += 1
# # # # #
# # # # #         print(x, 499.2e6 * 128.0 * 17.2, 2 ** 40)
# # # # #     except:
# # # # #         ...
# # # # #     break
# # # # # print(0.15 * 499.2e6 * 128.0)
# # # # # print(struct.pack('B',266))
# # # # import datetime
# # # # #
# # # # # a = datetime.datetime.now().second
# # # # # b = datetime.datetime.now().second
# # # # # q = 0
# # # # # while True:
# # # # #     q += 1
# # # # #     b = datetime.datetime.now().second
# # # # #     if b - a == 10:
# # # # #         break
# # # # # print(a, b, q)
# # # #
# # # # # a=0b1111111111111111111111111111111111111111
# # # # # print(a, struct.pack('Q',a))
# # # # #
# # # # # def a():
# # # # #     cou.set1(100)
# # # # # print(datetime.datetime.now())
# # # # # t=datetime.datetime.now()
# # # # # # for i in range(10000):
# # # # # #     filename = unit.BASE_DIR + "\data\Bilk_data.json"
# # # # # #     json1 = unit.read_name_data(filename, "Tag_Addr")
# # # # # #     print(json1[0][0])
# # # # # print(datetime.datetime.now()-t)
# # # # # filename = unit.BASE_DIR + "\data\Bilk_data.json"
# # # # # with open(filename, 'rb') as f:
# # # # #     params = json.load(f)
# # # # #     params['sep'] = cou.Sep1
# # # # # f.close()
# # # # # json1 = unit.read_name_data(filename, "Tag_Addr")
# # # # # print(json1['sep'][0])
# # # # # json_path1=unit.BASE_DIR + "\data\sep.json"
# # # # # json_path=unit.BASE_DIR + "\data\sep.json"
# # # # # def get_json_data(json_path):
# # # # #     # 获取json里面数据
# # # # #
# # # # #     with open(json_path, 'rb') as f:
# # # # #         # 定义为只读模型，并定义名称为f
# # # # #
# # # # #         params = json.load(f)
# # # # #         # 加载json文件中的内容给params
# # # # #
# # # # #         params['sep'] = 16
# # # # #         # 修改内容
# # # # #
# # # # #         print("params", params)
# # # # #         # 打印
# # # # #
# # # # #         dict = params
# # # # #         # 将修改后的内容保存在dict中
# # # # #
# # # # #     f.close()
# # # # #     # 关闭json读模式
# # # # #
# # # # #     return dict
# # # # #     # 返回dict字典内容
# # # # #
# # # # #
# # # # # def write_json_data(dict):
# # # # #     # 写入json文件
# # # # #
# # # # #     with open(json_path1, 'w') as r:
# # # # #         # 定义为写模式，名称定义为r
# # # # #
# # # # #         json.dump(dict, r)
# # # # #         # 将dict写入名称为r的文件中
# # # # #
# # # # #     r.close()
# # # # #     # 关闭json写模式
# # # #
# # # # d=cou.BINK(500,500,4)
# # # # print(d)
# # # # # the_revised_dict = get_json_data(json_path)
# # # # # write_json_data(the_revised_dict)
# # # # # json_path1=unit.BASE_DIR + "\data\sep.json"
# # # # # json1 = unit.get_json_data(json_path1 )
# # # # # print(json1["sep"])
# # # # # 调用两个函数，更新内容
# # # # t=191726963287-191729143135
# # # # print(t,t*299702547/ 499.2e6 * 128.0,499.2e6 * 128.0)
# # # # print(100/299702547*499.2e6 * 128.0,cou.BINK(10000, 111111111 , 0))
# # # #
# # # # print(24060974 / (63897600000*299702547), cou.sqr(10000),20000000*299702547/(499.2e6 * 128.0))
# # # #
# # # #
# # # #
# # # # print(4780054-4642331,4849678-4780054,4953666-4849678,5384500-4953666)
# # # #
# # # # print(4780054-9585384562)
# # # #
# # # #
# # # #
# # # # def time_x():
# # # #     t = 0b0000000000000000000000000000000011001010
# # # #     while True:
# # # #         if t > 1099511627775:
# # # #             t = 0b0000000000000000000000000000000000000000
# # # #
# # # #             print(t,datetime.datetime.now())
# # # #             break
# # # #         print(bin(t))
# # # #         t += 1
# # # #
# # # # t1=datetime.datetime.now()
# # # # print( '开始',datetime.datetime.now())
# # # # # time_x()
# # # # t2=datetime.datetime.now()
# # # # print( '结束',datetime.datetime.now())
# import threading
#
#
# def ad(id):
#     import xinxi8
#     st=xinxi8.chor()
#     st.start(id)
#
#
# t3 = threading.Thread(target=ad,args=(4,))
# t3.start()
# t2 = threading.Thread(target=ad,args=(3,))
# t2.start()
# t1 = threading.Thread(target=ad,args=(2,))
# t1.start()
#  # # #
# # # import multiprocessing
# # # def puts(queue):
# # #     queue.put("今天又是丧丧的一天呢")#简单的理解为put传入数据
# # # if __name__ == '__main__':
# # #     queue = multiprocessing.Queue(maxsize=9)#Queue方法设置最大传输字节数，maxsize可以不加，但是括号里一定要写数值否则无法实现
# # #     for n in range(5):
# # #         t1 = multiprocessing.Process(target=puts,args=(queue,))
# # #         t1.start()
# # #         t1.join()
# # #     print(queue.get())#接收传入值，如果get后无()则输出地址
# # # import multiprocessing
# # #
# # #
# # # # 写数据任务
# # # def write(queue):
# # #     for i in range(10):
# # #         if queue.full():
# # #             print('已经满员，不能再存')
# # #             break
# # #         queue.put(i)
# # #
# # #
# # # # 读取任务
# # # def read(queue):
# # #     while True:
# # #         if queue.empty():
# # #             print('没有值啦')
# # #             break
# # #         print(queue.get(),888)
# # #
# # # def read2(queue):
# # #     while True:
# # #         if queue.empty():
# # #             print('没有值啦')
# # #             break
# # #         print(queue.get())
# # #
# # #
# # # if __name__ == '__main__':
# # #     queue = multiprocessing.Queue(0)
# # #     t1 = multiprocessing.Process(target=write, args=(queue,))
# # #     t2 = multiprocessing.Process(target=read, args=(queue,))
# # #     t3 = multiprocessing.Process(target=read2, args=(queue,))
# # #     t1.start()
# # #     t1.join()
# # #     t2.start()
# # #     t3.start()
# # import cou
# # import unit
# #
# # filename = unit.BASE_DIR + "\data\Bilk_data.json"
# #
# #
# # # json1 = unit.read_name_data(filename, "Tag_Addr")
# # # json2 = unit.read_name_data(filename, "Blik_time")
# # # json3 = unit.read_name_data(filename, "XYZ")
# # # print(json3[0][1][0])
# # # X1 = json3[0][0][0]
# # # Y1 = json3[0][0][1]
# # # Z1 = json3[0][0][2]
# # # X2 = json3[0][1][0]
# # # Y2 = json3[0][1][1]
# # # Z2 = json3[0][1][2]
# # # X3 = json3[0][2][0]
# # # Y3 = json3[0][2][1]
# # # Z3 = json3[0][2][2]
# # #
# # # print(X1,X2,X3,json1)
# # # # X=json3[0][0]
# # # # Y=json3[0][1]
# # # # print(cou.BINK(X, Y, 1), cou.BINK(X, Y, 2), cou.BINK(X, Y, 3), cou.BINK(X, Y, 4))
# # # # print(cou.BINK(80, 80, 1), cou.BINK(80, 80, 2), cou.BINK(80, 80, 3), cou.BINK(80, 80, 4))

import paramiko
import logging
import sys
import os

# 加入日志
# 获取logger实例
logger = logging.getLogger("baseSpider")
# 指定输出格式
formatter = logging.Formatter('%(asctime)s\
              %(levelname)-8s:%(message)s')
# 文件日志
file_handler = logging.FileHandler("operation_theServer.log")
file_handler.setFormatter(formatter)
# 控制台日志
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)

# 为logge添加具体的日志处理器
logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.setLevel(logging.INFO)

class TheServerHelper():
    """初始化函数构造
        其中remote有两个作用，除了字面的服务器路径外
        还作为执行的语句"""
    def __init__(self,serverIP,username,password,remote,local_dir='',ftpType='',port=22):
        self.serverIP = serverIP
        self.username = username
        self.password = password
        self.port = port
        self.ftpType = ftpType
        self.remote = remote
        self.local_dir = local_dir


    #SSH连接服务器，用于命令执行
    def ssh_connectionServer(self):
        try:
            # 创建SSH对象
            sf = paramiko.SSHClient()
            # 允许连接不在know_hosts文件中的主机
            sf.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # 连接服务器
            sf.connect(hostname=self.serverIP, port=self.port, username=self.username,
                                          password=self.password)
            stdin, stdout, stderr = sf.exec_command(self.remote)
            # stdin, stdout, stderr = sf.exec_command('cd path;pwd' + ';' + shell, get_pty=True)
            # while True:
            result1 = stdout.read()

            print(result1 )
        except:
            logger.error("SSHConnection" +self.serverIP+"failed!")
            return False
        return True


    #FTP连接服务器，用于文件上传和下载
    def ftp_connectionServer(self):
        try:
            # 创建ftp对象
            sf = paramiko.Transport(self.serverIP, self.port)
            sf.connect(username=self.username,password=self.password)
            sftp = paramiko.SFTPClient.from_transport(sf)
        except:
            logger.error("FTPConnection "+self.serverIP+" failed!")
            return False
        """定义参数ftpType：
                    ftpType=1    单个文件从其他服务器向本地下载
                    ftpType=2    单个文件向服务器上传
                    ftpType=3    文件夹下内容下载
                    ftpType=4    文件夹下内容上传"""
        local_path = os.path.dirname(self.local_dir)
        if self.ftpType==1:
            if not os.path.exists(local_path):
                os.makedirs(local_path)
                sftp.get(self.remote,self.local_dir)
                sf.close()
                return True
        elif self.ftpType==2:
            sftp.put(self.local_dir,self.remote)
            sf.close()
            return True
        else:
            logger.error("服务器路径："+self.remote+"本地路径："+self.local_dir)
            return False
TheServerHelper=TheServerHelper("10.10.90.33",'test','Cmcc2020','cd le/cle/'+';'+'ls'+';'+'./cmsr-le_v1.1 ')

TheServerHelper.ssh_connectionServer()
# TheServerHelper.ftp_connectionServer()