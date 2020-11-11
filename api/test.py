import socket
import threading
import os
import time
import unittest

import unit


def anchor():
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    filename = unit.BASE_DIR + "\data\Bilk_data.json"
    json = unit.get_json_data(filename)
    sk.connect((json["ip"], json['chor_port']))

    XML='<req type="anchor cfg"><anchor addr="01aa6083cf111111" x="0"' \
        ' y="0" z="0" syncref="1" follow_addr="0" lag_delay="0"></anchor>' \
        '<anchor addr="01aa6083cf222222" x="200" y="0" z="0" ' \
        'syncref="0" follow_addr="0" lag_delay="0"><syncrefanchor ' \
        'addr="01aa6083cf111111" rfdistance="0"/></anchor>' \
        '<anchor addr="01aa6083cf333333" x="200" y="200" z="0" syncref="0" ' \
        'follow_addr="0" lag_delay="0"><syncrefanchor addr="01aa6083cf111111" ' \
        'rfdistance="0"/></anchor><anchor addr="01aa6083cf444444" x="0" y="200" z="0" ' \
        'syncref="0" follow_addr="0" lag_delay="0"><syncrefanchor addr="01aa6083cf111111" ' \
        'rfdistance="0"/></anchor></req>'
    sk.send(XML.encode('utf-8'))
    msg=sk.recv(1024)
    print("基站配置结果：", str(msg, 'utf8'))


def sonck1():
    os.system('python D:\\socket\\api\\xinxi.py')

def sonck2():
    os.system('python D:\\socket\\api\\xinxi2.py')

def sonck3():
    os.system('python D:\\socket\\api\\xinxi3.py')

def sonck4():
    os.system('python D:\\socket\\api\\xinxi4.py')

# anchor()
#四个线程同时对应并发运行以下4个基站
t1 = threading.Thread(target=sonck1)

t2 = threading.Thread(target=sonck2)

t3 = threading.Thread(target=sonck3)

t4 = threading.Thread(target=sonck4)
t1.start()
t2.start()
t3.start()
t4.start()
# anchor()
# time.sleep(1)
#对四个基站进行坐标配置和主基站次基站配置

