import datetime
import socket
import cou
import unit
from api.sk2 import xintiao, zhuce, CCPTX_Report, CCPRX_Report, BLINK_Report
import threading
import time
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
Rx_seq=0
tts=0
Blink_seq=0
Blink_tts=0
filename = unit.BASE_DIR + "\data\Data.json"
anchor_cfg_list = unit.read_name_data2(filename, "anchor_cfg")
list = []
for i in anchor_cfg_list:
    list.append(i)
# 分类接受打印引擎返回信息
def Recv_info(ms):
    # print('分类接收打印引擎返回信息', ms)
    global bs

    try:
        if ms == b'':
            ...
        elif ms == 0 or ms == None:
            print("连接失败")
        elif ms[0] == 0x21:
            ...

            # print("基站心跳包2：",hex(ms[0]),ms)
        elif ms[0] == 0x43:
            print("配置基站2定位参数：",hex(ms[0]),hex(ms[1]),hex(ms[2]))
        elif ms[0] == 0x44:
            print("配置基站2射频参数：",hex(ms[0]))
        elif ms[0] == 0x57:
            cou.rtls = 1
            print('2定位开始：', hex(ms[0]), ms[1])
            if ms[1]==1:
                bs=1
            elif ms[1]==0:
                bs=0
            else:
                bs=3
        elif ms[0] == 0x45:
            print("配置基站2天线延迟参数：",hex(ms[0]) )
        else:
            print(" 2其他参数：", hex(ms[0]))
            # ms.hex().encode(encoding="utf-8"))
    except Exception as e:
        print('服务器连接失败--2', e)

# 标签信息 无返回值
def Blink_info():
    # 读取标签的addr文件
    filename = unit.BASE_DIR + "\data\Data.json"
    json1 = unit.read_name_data2(filename, "Tag_Addr_XYZ")
    # json2 = unit.read_name_data(filename, "Blik_time")
    # Blink_time=1/float(json2[0][0])
    # print('2基站Blink发送频率为:{}HZ'.format(json2[0][0]))
    X=-1
    aaa=0
    while True:
            sep_c = Blink_seq
            time1 = Blink_tts
            if   X != sep_c:
                # print(sep_c)
                aaa+=1
                try:
                    n = 0
                    for Tag_Addr in json1:
                        tt = time1+ cou.BINK(Tag_Addr[1][0], Tag_Addr[1][1], 2,list) - cou.BINK(
                            Tag_Addr[1][0], Tag_Addr[1][1], 1,list)
                        sk.send(BLINK_Report(sep_c, Tag_Addr[0], tt))
                        n += 1

                    X = sep_c
                except Exception as e:
                    print('服务器连接失败--222', e)

# 在启动TDOA定位后，所有的基站都会向定位引擎发送时间同步包接收报告
def CCPRX_Report2():
    Rxseq = -1
    x=0
    while True:
        while True:
            x=Rx_seq
            if Rxseq!=x:
                try:
                    t=tts+ cou.BINK(list[1][1][0], list[1][1][1], 0,list)
                    # print('CCPTX_Report2----', x, t)
                    sk.send(CCPRX_Report(x, t,list[0][0]))
                    cou.time2=t
                    # t = cou.time3 + int(0.15 * 499.2e6 * 128.0)
                    Rxseq = Rx_seq
                    break
                except Exception as e:
                    print('CCPRX_Report2', e)
            else:
                ...
#计时器
def time_x():

    t = 0b0000000000000000000000000000001100000011
    while True:
        if t >= 1099511627775:
            t = 0b0000000000000000000000000000000000000000
            cou.time2=0
        # report_name = os.path.dirname(os.path.abspath(__file__)) + "/report/test_info.html"
        # time.sleep(0.1)
        cou.time2=cou.time2+1

        t+=1

# 心跳间隔是2秒 2秒发送一个心跳包并且收到引擎一个心跳回访 一旦超时未收到双方连接立即中断
def xintiao2():
    i = 0
    while True:
      try:
        sk.send(xintiao())
        ms = sk.recv(1024)
        Recv_info(ms)
        i += 1
        time.sleep(5)
      except Exception as e:
          print('服务器连接失败--2', e)
          break


while True:
    try:
        filename = unit.BASE_DIR + "\data\Data.json"
        json = unit.get_json_data(filename)
        sk.connect((json["ip"],json['port']))
        sk.send(zhuce(list[1][0]))
        # print('次基站2注册信息包', zhuce())

        ms = sk.recv(1024)
        Recv_info(ms)
        ## 属于线程t的部分
        t1 = threading.Thread(target=xintiao2)
        t2 = threading.Thread(target=Blink_info)
        t3 = threading.Thread(target=CCPRX_Report2)
        # t4 = threading.Thread(target=time_x)
        t1.start()
        # t4.start()

        while True:
            if cou.rtls==1:
                t3.start()
                t2.start()
                break
        break
    except Exception as e:
        print('服务器连接失败--', e)

## 属于线程t的部分
# t1.join() # join是阻塞当前线程(此处的当前线程时主线程) 主线程直到Thread-1结束之后才结束
# t2.join()


