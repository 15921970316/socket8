import json
import math

import unit

Sep1=0
Sep2=0
Sep3=0
Sep4=0

aaaa=0
ts1=0
ts2=0
ts3=0
ts4=0

time=0
time2=0
time3=0
time4=0
rtls =0

Rx_seq=0
Blink_seq=0
tts=0
#坐标时间戳函数  X代表横坐标 Y代表纵坐标 id代表基站编号 id为零代表求该基站到原点（0,0）的距离的时间戳
def BINK(x,y,id):
    if id==1:
        return int( math.sqrt(x*x+y*y) /299702547* 499.2e6 * 128.0)
    elif id==2:
        return int( math.sqrt((10-x)*(10-x)+y*y) /299702547* 499.2e6 * 128.0)
    elif id==3:
        return int( math.sqrt((10-x)*(10-x)+(10-y)*(10-y)) /299702547* 499.2e6 * 128.0)
    elif id==4:
        return int( math.sqrt(x*x+(10-y)*(10-y)) /299702547* 499.2e6 * 128.0)

    elif id==0 and y==0:
        return int((x/299702547)* (499.2e6 * 128.0))
    elif id==0 and x==0:
        return int((y/299702547)* (499.2e6 * 128.0))
    elif id==0 and x!=0 and y!=0:
        return int( math.sqrt(x*x+y*y) /299702547* 499.2e6 * 128.0)
# a=55
# print(abs(a))
# print(BINK(5, 5, 4) - BINK(5, 5, 1))
def sqr(d):
    z = d / 299702547* 499.2e6 * 128.0
    x = (d/299702547)* (499.2e6 * 128.0)
    return int(z)


class GlobalVar:
    db_handle = None
    mq_client = None


def set_db_handle(db):
    GlobalVar.db_handle = db


def get_db_handle():
    return GlobalVar.db_handle


def set_mq_client(mq_cli):
    GlobalVar.mq_client = mq_cli


def get_mq_client():
    return GlobalVar.mq_client


def set1(t):
    set_mq_client(t)

def get1():

    return str(get_mq_client())


class time_x():
    def settime(self,x):
        global a

        a=x
    def gettime(self):
        return a

json_path1=unit.BASE_DIR + "\data\sep.json"
json_path=unit.BASE_DIR + "\data\sep.json"
def get_json_data(json_path,sep):
    # 获取json里面数据

    with open(json_path, 'rb') as f:
        # 定义为只读模型，并定义名称为f

        params = json.load(f)
        # 加载json文件中的内容给params

        params['sep'] = sep
        # 修改内容

        # print("params", params)
        # 打印

        dict = params
        # 将修改后的内容保存在dict中

    f.close()
    # 关闭json读模式

    return dict
    # 返回dict字典内容


def write_json_data(dict):
    # 写入json文件

    with open(json_path1, 'w') as r:
        # 定义为写模式，名称定义为r

        json.dump(dict, r)
        # 将dict写入名称为r的文件中

    r.close()
    # 关闭json写模式


