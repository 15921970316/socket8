import socket
import time
import datetime
# 获取socket对象，括号里默认是AF_INET  和 SOCK_STREAM  所以可以不写
import unit


class Test_api():

    def __init__(self):
        # 初始化连接
        self.sk = socket.socket()

        try:
            self.sk.connect(('10.14.1.88', 59334))  # 链接到服务器端 括号里也是一个元组，包含ip地址以及对方的端口号
            unit.server_state = 1
            print("打开连接！")
        except Exception as e:
            unit.server_state = -1
            print("服务器连接失败：请检查网络连接或者服务端是否启动！状态码：-1", e)
        # self.sk.settimeout(5)

    def yq_response(self, instruct):
        self.msg = []
        try:  # 为了防止服务器非正常下线而导致客户端直接崩溃，需要加入异常处理
            # 发送传参的指令instruct
            # instruct= bytes('[00000010 01000000 00000000 01000010 10010011 00000101 10010010 11001111 10000011 01100000 10101010 00000001 01010110 01000101 01010010 01010011 01001001 01001111 01001110 00111010 00110100 00101110 00110001 00110100 00101110 00110010 00110000 00110000 00110100 00110010 00111000 00100000 01000011 01001111 01001101 01010000 01001001 01001100 01000101 01000100 00111010 01000001 01110000 01110010 00100000 00110010 00111000 00100000 00110010 00110000 00110010 00110000 00100000 00110001 00111001 00111010 00110001 00110101 00111010 00110001 00110110 00000000 00000000 00000000 00000000 00000000 00000000 00010100 11010110 00000011]')
            self.sk.send(instruct.encode('utf-8'))
            # 接收返回信息
            self.msg = self.sk.recv(1024)
            unit.server_state = 1
        except Exception as e:
            unit.server_state = -1
            print(e)
            return e
        # 返回响应信息
        return self.msg

    #  通信测试
    def yq_response2(self, instruct):
        self.msg = []
        data = []
        try:  # 为了防止服务器非正常下线而导致客户端直接崩溃，需要加入异常处理
            # 发送传参的指令instruct
            self.sk.send(instruct.encode('utf-8'))
            t1 = time.time()

            # 接收返回信息
            while True:
                self.msg = self.sk.recv(1024)

                data.append(self.msg)
                if 'starts' in str(self.msg, 'utf8'):
                    print("开始啦", datetime.datetime.now())

                if 'completes' in str(self.msg, 'utf8'):
                    print("测距结束啦", datetime.datetime.now())
                    break

                if 'msg="comm test starts">' in str(self.msg, 'utf8'):
                    print("通信测试开始啦", datetime.datetime.now())

                if 'msg = "comm test completes"' in str(self.msg, 'utf8'):
                    print("通信测试结束啦", datetime.datetime.now())
                    break
                unit.server_state = 1
            t2 = time.time()
            print('测试用了时间：{}秒'.format(t2 - t1))
        except Exception as e:
            unit.server_state = -1
            print(e)
        # 返回响应信息
        return data

    # 功率测试的函数
    def yq_response3(self, instruct):
        self.msg = []
        data = []
        try:  # 为了防止服务器非正常下线而导致客户端直接崩溃，需要加入异常处理
            # 发送传参的指令instruct
            self.sk.send(instruct.encode('utf-8'))

            # 接收返回信息

            while self.sk.settimeout(2) != 'timed out':
                while True:
                    self.msg = self.sk.recv(1024)

                    data.append(self.msg)
                    if 'system' in str(self.msg, 'utf8'):
                        continue
                        # print("{}测试开始啦".format(i), datetime.datetime.now())

                    if 'power' in str(self.msg, 'utf8'):
                        # print("{}测试结束啦".format(i), datetime.datetime.now())
                        break
                    if 'not' in str(self.msg, 'utf8'):
                        # print("{}测试结束啦".format(i), datetime.datetime.now())
                        break

            unit.server_state = 1
        except Exception as e:
            unit.server_state = -1
            print(e)
        # 返回响应信息
        return data

    # 参数错误情况功率测试的函数
    def yq_response3_error(self, instruct):
        self.msg = []
        data = []
        try:  # 为了防止服务器非正常下线而导致客户端直接崩溃，需要加入异常处理
            # 发送传参的指令instruct
            self.sk.send(instruct.encode('utf-8'))

            # 接收返回信息
            i = 1

            while True:
                self.msg = self.sk.recv(1024)
                data.append(self.msg)
                if 'system' in str(self.msg, 'utf8'):
                    ...
                    # print("{}测试开始啦".format(i), datetime.datetime.now())
                if 'done' in str(self.msg, 'utf8'):
                    continue
                if 'status="not connected"/></ind>' in str(self.msg, 'utf8'):
                    # print("{}测试结束啦".format(i), datetime.datetime.now())
                    break

            unit.server_state = 1
        except Exception as e:
            unit.server_state = -1
            print(e)
        # 返回响应信息
        return data

    def close(self):
        print("关闭连接！")
        self.sk.close()  # 关闭socket对象
