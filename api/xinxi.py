import socket
import unit

from api.sk import xintiao, zhuce, CCPTX_Report, CCPRX_Report, BLINK_Report
import threading
import time
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
import cou
import datetime
s = 0

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
            print("配置基站1定位参数：",hex(ms[0]),hex(ms[1]),hex(ms[2]))
        elif ms[0] == 0x44:
            print("配置基站1射频参数：",hex(ms[0]))
        elif ms[0] == 0x57:
            print('1定位开始：', hex(ms[0]), ms[1])
            cou.rtls=1

            if ms[1]==1:
                bs=1
            elif ms[1]==0:
                bs=0
            else:
                bs=3
        elif ms[0] == 0x45:
            print("配置基站1天线延迟参数：",hex(ms[0]) )
        else:
            print(" 其他参数：", hex(ms[0]))
            # ms.hex().encode(encoding="utf-8"))
    except Exception as e:
        print('服务器连接失败--1', e)

# 标签信息 无返回值
def Blink_info():
    print(datetime.datetime.now(), 'Blink_info')
    #读取标签的addr文件
    filename = unit.BASE_DIR + "\data\Bilk_data.json"
    json1 = unit.read_name_data(filename, "Tag_Addr")
    json2 = unit.read_name_data(filename, "Blik_time")
    Blink_time=1/float(json2[0][0])
    json_path = unit.BASE_DIR + "\data\sep.json"
    print('1基站Blink发送频率为:{}HZ'.format(json2[0][0]))
    t=0
    sep = 0

    while True:
        try:
            if sep >255:
               sep = 0
               # print('我到了255了 bink1')
            j=0
            time1 = cou.time
            for Tag_Addr in json1[0]:
                sk.send(BLINK_Report(sep, Tag_Addr,time1))
                j+=1
                print('Blink_info1----',sep, Tag_Addr,time1)
            xinxi2.Blink_seq=sep
            xinxi3.Blink_seq=sep
            xinxi4.Blink_seq=sep
            sep+=1
            if sep == 256:
                sep = 0
            time.sleep(Blink_time)

        except    Exception as e:
            print('服务器连接失败--1111', e)

# 在启动TDOA定位后，所有的基站都会向定位引擎发送时间同步包接收报告
def CCPTX_Report1():
    t = 0+cou.time
    Txseq=0
    while True:
        try:
            if Txseq >255:
               Txseq = 0
               # print('我到了255了 ccp1')
            t=cou.time
            # t = t + int(0.15 * 499.2e6 * 128.0)
            if t > 1099511627775:
                cou.time =0
                # t = cou.time + int(0.15 * 499.2e6 * 128.0)
            sk.send(CCPTX_Report(Txseq, t))
            xinxi2.Rx_seq = Txseq
            xinxi3.Rx_seq = Txseq
            xinxi4.Rx_seq = Txseq
            xinxi2.tts = t
            xinxi3.tts = t
            xinxi4.tts = t
            # cou.time=t
            print('CCPTX_Report1----', Txseq, t )
            time.sleep(0.15)

            Txseq += 1
            if Txseq==256:
                Txseq=0
        except Exception as e:
            print('CCPTX_Report1',e)

#计时器
def time_x():
    filename = unit.BASE_DIR + "/data/time.txt"

    t = 0b0000000000000000000000000000000000000000
    cou.time =0
    while True:
        if t >= 1099511627775:
            t = 0b0000000000000000000000000000000000000000
            cou.time=0
        # report_name = os.path.dirname(os.path.abspath(__file__)) + "/report/test_info.html"
        # time.sleep(0.1)
        cou.time = cou.time + 1
        time.sleep(0.01)
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
        time.sleep(2)
      except Exception as e:
          print('服务器连接失败--1', e)
          break
def anchor():
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    filename = unit.BASE_DIR + "\data\Bilk_data.json"
    json = unit.get_json_data(filename)
    sk.connect((json["ip"], json['chor_port']))

    XML='<req type="anchor cfg"><anchor addr="01aa6083cf111111" x="0"' \
        ' y="0" z="0" syncref="1" follow_addr="0" lag_delay="0"></anchor>' \
        '<anchor addr="01aa6083cf222222" x="10" y="0" z="0" ' \
        'syncref="0" follow_addr="0" lag_delay="0"><syncrefanchor ' \
        'addr="01aa6083cf111111" rfdistance="0"/></anchor>' \
        '<anchor addr="01aa6083cf333333" x="10" y="10" z="0" syncref="0" ' \
        'follow_addr="0" lag_delay="0"><syncrefanchor addr="01aa6083cf111111" ' \
        'rfdistance="0"/></anchor><anchor addr="01aa6083cf444444" x="0" y="10" z="0" ' \
        'syncref="0" follow_addr="0" lag_delay="0"><syncrefanchor addr="01aa6083cf111111" ' \
        'rfdistance="0"/></anchor></req>'
    sk.send(XML.encode('utf-8'))
    msg=sk.recv(1024)
    print("基站配置结果：", str(msg, 'utf8'))


while True:
    try:
        filename = unit.BASE_DIR + "\data\Bilk_data.json"
        json = unit.get_json_data(filename)
        sk.connect((json["ip"],json['port']))
        sk.send(zhuce())
        ms = sk.recv(1024)
        Recv_info(ms)
        ## 属于线程t的部分
        t1 = threading.Thread(target=xintiao2)
        t2 = threading.Thread(target=Blink_info)
        t3 = threading.Thread(target=CCPTX_Report1)
        t4 = threading.Thread(target=time_x)
        # t5 = threading.Thread(target=canshu)
        t1.start()
        anchor()
        t4.start()
        from api import xinxi3, xinxi4, xinxi2

        while True:
            if cou.rtls==1:
                t3.start()
                # # t5.start()
                t2.start()
                break
        break
    except Exception as e:
        print(e)
## 属于线程t的部分
# t1.join() # join是阻塞当前线程(此处的当前线程时主线程) 主线程直到Thread-1结束之后才结束
# t2.join()


