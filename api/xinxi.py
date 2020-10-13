import socket
import struct
import threading
import time
from api.sk import xintiao, zhuce, CCPTX_Report, CCPRX_Repor, BLINK_Report
from datetime import datetime

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try:
    # sk.bind(('10.10.90.17', 15534))  # 自己的端口号设置
    # sk.connect(('10.10.90.17', 59335))  # 链接到服务器端 括号里也是一个元组，包含ip地址以及服务器的端口号
    sk.connect(('10.14.1.88', 59336))


    # print('注册信息：',zhuce())
except Exception as e:
    print('服务器连接失败--', e)
    ms = 0


# 分类接受打印引擎返回信息
def Recv_info(ms):
    print('分类接受打印引擎返回信息')

        # 心跳间隔是2秒 2秒发送一个心跳包并且收到引擎一个心跳回访 一旦超时未收到双方连接立即中断

    if ms == 0 or ms ==None:
         print("连接失败")
    elif ms[0] == 0x21:
        print("基站心跳包：", datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3], "\n\t", ms)
    elif ms[0] == 0x43:
        print("配置基站定位参数：", datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3], "\n\t",
              ms.hex().encode(encoding='utf8'))
    elif ms[0] == 0x44:
        print("配置基站射频参数：", datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3], "\n\t",
              ms.hex().encode(encoding="utf-8"))
    elif ms[0] == 0x45:
        print("配置基站天线延迟参数：", datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3], "\n\t",
              ms.hex().encode(encoding="utf-8"))
    else:
        print(" 其他参数：", datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3], "\n\t",
              ms.hex().encode(encoding="utf-8"))


# 标签信息
def Blink_info():
    sk.send(zhuce())  # 注册信息

    Seq = 0
    while True:
        if Seq == 255:
            Seq = 0
        # print(xintiao())
        # sk.send(xintiao())
        # ms = sk.recv(1024)
        # Recv_info(ms)
        sk.send(CCPTX_Report(Seq))
        sk.send(CCPRX_Repor(Seq))
        sk.send(BLINK_Report(Seq))
        ms=sk.recv(1024)
        # Recv_info(ms)
        Seq += 1



# 心跳
def xintiao2():
    i = 0
    while True:
        sk.send(xintiao())
        ms=sk.recv(1024)
        Recv_info(ms)
        i += 1
        time.sleep(1)

sk.send(zhuce())
xintiao2()
# from time import sleep, ctime
# import threading
# threads = []
# t = threading.Thread(target=xintiao2 )
# threads.append(t)
# t = threading.Thread(target=Blink_info )
# threads.append(t)
# if __name__ == '__main__':
#     #启动线程
#
#     threads[0].start()
#     threads[1].start()
#
#     threads[0].join()
#     threads[1].join()
#
#     #主线程
#     print('end:%s' %ctime())
# xintiao2()
import multiprocessing  as mp
# group ：group参数并不使用；
# target：表示调用对象，即该进程要执行的任务，或者说是传入一个方法；
# name ： 进程的别名；
# args ： srgs是一个元组，它里面是调用target方法需要传入的参数；
# kwargs：kwargs是一个字典，它里面是调用target方法需要传入的关键字参数；
# if __name__ == "__main__":
#     pool=mp.Pool()
#     res1=pool.apply_async(xintiao2,)
#     res2 = pool.apply_async(Blink_info, )
#     res3 = pool.apply_async(Recv_info, )
#     print(res1.get())
#     pool.close()  # 关闭进程池，表示不能在往进程池中添加进程
#     pool.join()  #
# from multiprocessing import Process
# Recv_info()
# Blink_info()
# p = Process(target=xintiao2(), args=('',))  # p进程执行f函数，参数为'bob'，注意后面的“,”
# # p2 = Process(target=Blink_info(), args=('',))  # p进程执行f函数，参数为'bob'，注意后面的“,”
# # p3 = Process(target=Recv_info(), args=('',))  # p进程执行f函数，参数为'bob'，注意后面的“,”
# p.start()  # 进程开始
#
# p.join()  # 阻塞主线程，直至p进程执行结束
# print('1111')
