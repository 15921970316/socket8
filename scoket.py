#客户端
import time
import socket
from datetime import datetime
# 获取socket对象，括号里默认是AF_INET  和 SOCK_STREAM  所以可以不写
sk = socket.socket()
# 链接到服务器端 括号里也是一个元组，包含ip地址以及对方的端口号
try:
    sk.connect(('10.14.1.88',59334))      # 自己的端口号系统会随机分配，不需要设置

    while True: # 收发信息也需要循环
        try: # 为了防止服务器非正常下线而导致客户端直接崩溃，需要加入异常处理

                # cmd = input("请输入消息内容....[输入Q退出对话]\n\t")
                # cmd='<req type="anchor list"/>'#获取基站列表命令
                cmd='<req type="rtls state"/>'#查询当前状态
                if cmd=='Q' or cmd=='q':  # 给客户端一个可以正常退出的方法
                    break

                if not cmd: # 如果直接敲回车，那么cmd就是空字符串，TCP协议对此进行优化
                    continue    # 正常收发消息过程中，你传入空字符串，它不会帮你发送
                sk.send(cmd.encode('utf-8'))
                # sk.send(cmd)

        # 如果上面没有做空判断，输入空会直接跳过send这步，这样客户端和服务器端都处于接收状态，卡住不动
                msg=sk.recv(1024)
                print("我：",datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3],"\n\t",cmd)
                print("服务器：",str(msg, 'utf8'))
                input("按任意键下一步")
        except Exception as e:
            print(e)
            break
    sk.close() # 关闭socket对象
except Exception as e:
    print(e)
