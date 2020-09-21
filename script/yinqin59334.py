# 测试用例
from api.jzyq_api import Test_api
import unittest
import time
import unit

# 基站配置

def anchor_cfg():
    print('对在线的基站进行配置命令:')
    addr=''
    syncref=''
    x=''
    y=''
    z=''
    # print(cls.status)
    # < req
    # type = "anchor cfg" > < anchor
    # addr = "1aa6083cf92080a"
    # x = "1.30"
    # y = "2.27"
    # z = "2.52"
    # syncref = "1"
    # follow_addr = "0"
    # lag_delay = "0" > < / anchor > < anchor
    # addr = "1aa6083cf920913"
    # x = "7.93"
    # y = "0.87"
    # z = "2.53"
    # syncref = "0"
    # follow_addr = "0"
    # lag_delay = "0" > < syncrefanchor
    # addr = "1aa6083cf92080a"
    # rfdistance = "0" / > < / anchor > < anchor
    # addr = "1aa6083cf91cb9d"
    # x = "8.04"
    # y = "10.43"
    # z = "2.56"
    # syncref = "0"
    # follow_addr = "0"
    # lag_delay = "0" > < syncrefanchor
    # addr = "1aa6083cf92080a"
    # rfdistance = "0" / > < / anchor > < anchor
    # addr = "1aa6083cf920a17"
    # x = "1.44"
    # y = "9.66"
    # z = "2.53"
    # syncref = "0"
    # follow_addr = "0"
    # lag_delay = "0" > < syncrefanchor
    # addr = "1aa6083cf92080a"
    # rfdistance = "0" / > < / anchor > < / req >
    addr1_right = "1aa6083cf920a17"  # 正确存在的基站
    addr2_right = "1aa6083cf920913"  # 正确存在的基站
    addr3_right = "1aa6083cf91cb9d"  # 正确存在的基站
    # addr4_right = "1aa6083cf920a17"  # 正确存在的基站
    # 指令
    instruct = '<req type="anchor cfg"><anchor addr="{}" x="1.30" y="2.27" z="2.52" syncref="1" ' \
               'follow_addr="0" lag_delay="0"></anchor>' \
               '<anchor addr="{}" x="7.93" y="0.87" z="2.53" syncref="0" follow_addr="0" lag_delay="0">' \
               '<syncrefanchor addr="{}" rfdistance="0"/></anchor>' \
               '<anchor addr="{}" x="8.04" y="10.43" z="2.56" ' \
               'syncref="0" follow_addr="0" lag_delay="0"><syncrefanchor addr="{}" rfdistance="0"/></anchor></req>'' '.format(
        addr1_right, addr2_right, addr1_right, addr3_right, addr1_right)

    print("请求的数据：", instruct)
    cls.msg = cls.oder.yq_response(instruct)
    # 断言配置设置未成功标识符status="not connected"已配置

    print("服务器返回的数据：", str(cls.msg, 'utf8'))
    cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(addr1_right),
                 str(cls.msg, 'utf8'))
    print("断言'{}'通过！".format(addr1_right))
    cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(addr2_right),
                 str(cls.msg, 'utf8'))
    print("断言'{}'通过！".format(addr2_right))
    cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(addr3_right),
                 str(cls.msg, 'utf8'))
    print("断言'{}'通过！".format(addr3_right))