# import time
# # import subprocess
# # import locale
# # import codecs
# #
# #
# # def getstdout(p):
# #     mylist = []
# #     while True:
# #         data = p.stdout.readline()
# #         if data == b'':
# #             if p.poll() is not None:
# #                 break
# #         else:
# #             mylist.append(data.decode(codecs.lookup(locale.getpreferredencoding()).name))
# #     return mylist
# #
# # while True:
# #     ps = subprocess.Popen('netstat -an | findstr "22"', stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
# #     resultlist = getstdout(ps)
# #     if len(resultlist) >= 1:
# #         print(resultlist)
# #     else:
# #         print(time.strftime("%Y-%m-%d %H:%M:%S"))
# #         subprocess.Popen('taskkill.exe /f /im node.exe', shell=False)
# # # 防止动作过快，把新建的程序整死了
# #         time.sleep(3)
# #         subprocess.Popen('start node D:\\app.js', shell=True)
# #     time.sleep(1)
import random
import subprocess

import paramiko, getpass  # getpass是隐藏密码

from unit import chor_count


def ssh_connect(password):
    host_ip = '10.10.90.199'
    user_name = 'test'
    host_port = '22'
    # 待执行的命令
    sed_command = " ls"
    ls_command = "cd /home/test/le/Logs;pwd "
    # ls_command2='/home/test/le/cle/./cmsr-le_v1.1 '
    ls_command2='ls'
    # 注意：依次执行多条命令时，命令之间用分号隔开
    command = sed_command + ";" + ls_command+';'+ls_command2
    # SSH远程连接
    ssh = paramiko.SSHClient()  # 创建sshclient
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 指定当对方主机没有本机公钥的情况时应该怎么办，AutoAddPolicy表示自动在对方主机保存下本机的秘钥
    ssh.connect(host_ip, host_port, user_name, password)
    # 执行命令并获取执行结果
    print(11)
    # command = "ls "
    # back = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    # print("back0----", back[0].decode())  # 注意需要进行解码操作，默认输出的是字节
    # print("back1----", back[1].decode())  # back是一个元祖，可以通过元祖取值的方式获取结果
    # while True:

    # out = stdout.readlines()
    # err = stderr.readlines()
    # print(out, err)
    stdin, stdout, stderr = ssh.exec_command(command)

    print(stdout.readlines())

    ssh.close()
    #
    # return out, err


if __name__ == '__main__':
    # pwd = input("请输入密码：")
    pwd="Cmcc2020"
    result = ssh_connect(pwd)
    # print(result)
# chor_count(10)
#
# ret = ""
# for i in range(6):
#     num = random.randint(0, 9)
#     # num = chr(random.randint(48,57))#ASCII表示数字
#     letter = chr(random.randint(97, 103))  # 取小写字母
#     Letter = chr(random.randint(65, 72))  # 取大写字母
#     s = str(random.choice([num, letter, Letter]))
#     ret += s
# print(ret)