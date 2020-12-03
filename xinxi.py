import multiprocessing
import socket
import unit
from api.sk import xintiao, zhuce, CCPTX_Report, CCPRX_Report, BLINK_Report
import threading
import time

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
import cou

s = 0
filename = unit.BASE_DIR + "\data\Data.json"

json2 = unit.read_name_data(filename, "Blik_time")
Blink_time = 1 / float(json2[0][0])

Rx_seq = 0
tts = 0
Blink_seq = 0
Blink_tts = 0


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
            # print("基站心跳包1：",ms)
        elif ms[0] == 0x43:
            print("配置基站1定位参数：", hex(ms[0]), hex(ms[1]), hex(ms[2]))
        elif ms[0] == 0x44:
            print("配置基站1射频参数：", hex(ms[0]))
        elif ms[0] == 0x57:
            print('1定位开始：', hex(ms[0]), ms[1])
            cou.rtls = 1

            if ms[1] == 1:
                bs = 1
            elif ms[1] == 0:
                bs = 0
            else:
                bs = 3
        elif ms[0] == 0x45:
            print("配置基站1天线延迟参数：", hex(ms[0]))
        else:
            print(" 其他参数：", hex(ms[0]))
            # ms.hex().encode(encoding="utf-8"))
    except Exception as e:
        print('服务器连接失败--1', e)


# 标签信息 无返回值
def Blink_info():
    x = 0
    # print(datetime.datetime.now(), 'Blink_info')
    # 读取标签的addr文件
    filename = unit.BASE_DIR + "\data\Data.json"

    json1 = unit.read_name_data2(filename, "Tag_Addr_XYZ")

    # print('Blink发送频率为:{}HZ'.format(json2[0][0]))
    t = 0
    sep = 0
    aaa = 0
    import datetime

    while True:
        data = datetime.datetime.now()
        # print(data)
        try:
            if sep > 255:
                sep = 0
            time2 = cou.time

            def blink():
                for Tag_Addr in json1:
                    # tt = cou.BINK(Tag_Addr[1][0], Tag_Addr[1][1], 1)
                    sk.send(BLINK_Report(sep, Tag_Addr[0], time2))

            def s():
                global Blink_seq
                Blink_seq = sep
                global Blink_tts
                Blink_tts = time2

            t1 = threading.Thread(target=blink)
            t2 = threading.Thread(target=s)
            t1.start()
            t2.start()
            sep += 1
            if sep == 256:
                sep = 0
        except    Exception as e:
            print('服务器连接失败--1111', e)
        # print('时间',datetime.datetime.now(),data-datetime.datetime.now())

        time.sleep(Blink_time)
        # print(Blink_time,'111111',aaa)
        aaa += 1


# 在启动TDOA定位后，所有的基站都会向定位引擎发送时间同步包接收报告
def CCPTX_Report1():
    t = 0 + cou.time
    Txseq = 0
    while True:
        try:
            if Txseq > 255:
                Txseq = 0
                # print('我到了255了 ccp1')
            t = cou.time
            if t > 1099511627775:
                cou.time = 0

            def ccp():
                sk.send(CCPTX_Report(Txseq, t))
                # print('主基站CCPTX：', Txseq, t)

            def s():
                global Rx_seq,tts
                Rx_seq = Txseq

                tts = t

            t1 = threading.Thread(target=s)
            t2 = threading.Thread(target=ccp)
            t2.start()
            t1.start()
            # cou.time=t
            # print('CCPTX_Report1----', Txseq, t )
            time.sleep(0.15)
            Txseq += 1
            if Txseq == 256:
                Txseq = 0
        except Exception as e:
            print('CCPTX_Report1', e)


# 计时器
def time_x():
    t = 0b0000000000000000000000000000000000000000
    cou.time = 0
    while True:
        if t >= 1099511627775:
            t = 0b0000000000000000000000000000000000000000
            cou.time = 0

        cou.time += 1000
        # print(cou.time)
        t += 1


# 心跳间隔是2秒 2秒发送一个心跳包并且收到引擎一个心跳回访 一旦超时未收到双方连接立即中断
def xintiao2():
    i = 0
    while True:
        sk.send(xintiao())
        # print('心跳：', xintiao())
        ms = sk.recv(1024)
        Recv_info(ms)
        i += 1
        time.sleep(2)


def anchor():
    sk2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sk2.connect((json["ip"], json['chor_port']))
    list1 = []
    j = 0
    XML = ''
    for i in anchor_cfg_list:
        list1.append(i)
        if j == 0:
            XML = '<req type="anchor cfg"><anchor addr="{}" x="{}" y="{}" z="0" syncref="1" follow_addr="0" lag_delay="0"></anchor>'.format(
                list[0][0], list[0][1][0], list[0][1][1])
        else:
            XML2 = '<anchor addr="{}" x="{}" y="{}" z="0" ' \
                   'syncref="0" follow_addr="0" lag_delay="0"><syncrefanchor ' \
                   'addr="{}" rfdistance="0"/></anchor>'.format(list1[j][0], list1[j][1][0], list1[j][1][1],
                                                                list1[0][0])
            XML = XML + XML2
        j += 1
    XML = XML + '</req>'

    sk2.send(XML.encode('utf-8'))
    sk2.recv(1024)
    xml2 = '<req type="rtls start"/>'
    # sk2.send(xml2.encode('utf-8'))
    # sk2.recv(1024)

    # print("基站配置结果：", str(msg, 'utf8'))

#次基站模块
def Base_station(id):
    # print("id为：", id)
    import socket
    from api.sk3 import xintiao, zhuce, CCPTX_Report, CCPRX_Report, BLINK_Report
    import time

    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 分类接受打印引擎返回信息
    def Recv_info(ms):
        # print('分类接收打印引擎返回信息', ms)
        global bs

        try:
            if ms == b'':
                ...
            elif ms == 0 or ms == None:
                print("连接失败{}：".format(id))
            elif ms[0] == 0x21:
                ...

                # print("基站心跳包3：",hex(ms[0]))
            elif ms[0] == 0x43:
                print("配置基站定位参数{}：".format(id), hex(ms[0]), hex(ms[1]), hex(ms[2]))
            elif ms[0] == 0x44:
                print("配置基站射频参数{}：".format(id), hex(ms[0]))
            elif ms[0] == 0x57:
                cou.rtls = 1
                print('定位开始{}：'.format(id), hex(ms[0]), ms[1])

                if ms[1] == 1:
                    bs = 1
                elif ms[1] == 0:
                    bs = 0
                else:
                    bs = 3
            elif ms[0] == 0x45:
                print("配置基站天线延迟参数{}：".format(id), hex(ms[0]))
            else:
                print(" 其他参数{}：".format(id), hex(ms[0]))
                # ms.hex().encode(encoding="utf-8"))
        except Exception as e:
            print('服务器连接失败{}：'.format(id), e)

    # 标签信息 无返回值
    def Blink_info():
        # 读取标签的addr文件
        filename = unit.BASE_DIR + "\data\Data.json"
        json1 = unit.read_name_data2(filename, "Tag_Addr_XYZ")
        X = -1
        while True:
            sep_c = Blink_seq
            time1 = Blink_tts
            try:
                n = 0
                for Tag_Addr in json1:
                    tt = time1 + cou.BINK(Tag_Addr[1][0], Tag_Addr[1][1], id, list) - cou.BINK(
                        Tag_Addr[1][0], Tag_Addr[1][1], 1, list)
                    sk.send(BLINK_Report(sep_c, Tag_Addr[0], tt))
                    n += 1
                    # print(id,sep_c)
                X = sep_c
                time.sleep(Blink_time)

            except Exception as e:
                print('服务器连接失败--444', e)

    # 在启动TDOA定位后，所有的基站都会向定位引擎发送时间同步包接收报告
    def CCPRX_Report3():
        Rxseq = -1
        while True:
            while True:
                x = Rx_seq

                try:
                    t = tts + cou.BINK(list[id-1][1][0], list[id-1][1][1], 0, list)
                    # print('CCPTX_Report{}----'.format(id), x, t)
                    sk.send(CCPRX_Report(x, t, list[0][0]))
                    cou.time4 = t
                    # t = cou.time3 + int(0.15 * 499.2e6 * 128.0)
                    Rxseq = Rx_seq
                    break
                except Exception as e:
                    print('CCPRX_Report4', e)
                time.sleep(0.15)
            # time.sleep(0.15)

    # 心跳间隔是2秒 2秒发送一个心跳包并且收到引擎一个心跳回访 一旦超时未收到双方连接立即中断
    def xintiao2():
        i = 0
        while True:
            try:
                # print(cou.time3)
                sk.send(xintiao())
                ms = sk.recv(1024)
                Recv_info(ms)
                i += 1
                time.sleep(2)
            except Exception as e:
                print('服务器连接失败--{}：'.format(id), e)
                break

    while True:
        try:
            filename = unit.BASE_DIR + "\data\Data.json"
            json = unit.get_json_data(filename)
            sk.connect((json["ip"], json['port']))
            # sk.connect(('10.14.1.88', 59336))
            sk.send(zhuce(list[id-1][0]))
            # print(list[id][0])
            # print('次基站3注册信息包:', zhuce())

            ms = sk.recv(1024)
            Recv_info(ms)
            ## 属于线程t的部分
            t1 = threading.Thread(target=xintiao2)
            t2 = threading.Thread(target=Blink_info)
            t3 = threading.Thread(target=CCPRX_Report3)
            # t4= threading.Thread(target=time_x)
            t1.start()
            # t4.start()
            while True:
                if cou.rtls == 1:
                    t3.start()
                    t2.start()
                    break
            break
        except Exception as e:
            print('服务器连接失败{}：'.format(id), e)



filename = unit.BASE_DIR + "\data\Data.json"
json = unit.get_json_data(filename)
try:
    sk.connect((json["ip"], json['port']))
    print('服务器连接成功！')

    t1 = threading.Thread(target=xintiao2)
    t1.start()
    chor_cou =  input('\n请输入需要随机的基站数量【直接按回车键则使用文件里原数据 】：')

    x = input('\n请输入需要随机的标签数量【直接按回车键则使用文件里原数据 】：')
    rate = input('\n请输入标签频率HZ【直接按回车键则使用文件里原数据 】：')
    if chor_cou == "":
        chor_cou = 0
    if x == "":
        x = 0
    if rate == "":
        rate = 0
    unit.chor_count(int(chor_cou))# 生成chor_cou个基站和随机的坐标

    unit.rw_xyz(int(x), int(rate))  # x随机生成x个坐标 设置标签频率rate
    anchor_cfg_list = unit.read_name_data2(filename, "anchor_cfg")
    print(len(anchor_cfg_list))
    list = []
    for i in anchor_cfg_list:
        list.append(i)
    sk.send(zhuce(list[0][0]))
    anchor()

    # print('主基站注册信息包:', zhuce())
    ms = sk.recv(1024)
    Recv_info(ms)
    ## 属于线程t的部分
    t2 = threading.Thread(target=Blink_info)
    t3 = threading.Thread(target=CCPTX_Report1)
    t4 = threading.Thread(target=time_x)
    t4.start()
    # import xinxi2, xinxi3, xinxi4,xinxi5
    for i in range(len(anchor_cfg_list) - 1):
        t = threading.Thread(target=Base_station, args=(i + 2,))
        t.start()
    while True:


        if cou.rtls == 1:
            t3.start()
            t2.start()



            break
except Exception as e:
    print(e,'11')

## 属于线程t的部分
# t1.join() # join是阻塞当前线程(此处的当前线程时主线程) 主线程直到Thread-1结束之后才结束
# t2.join()
