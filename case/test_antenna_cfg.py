#定位天线延迟配置 测试用例
from api.anchor_cfg import anchor_cfgs
from api.jzyq_api import Test_api
import unittest
import time
import unit

filename = unit.BASE_DIR + "\data\engine_Data.json"
# 定位天线延迟配置
class Test_antenna_cfg(unittest.TestCase):
    status = 99

    @classmethod
    def setUpClass(cls):
        cls.oder = Test_api()
        cls.status = unit.server_state
        cls.msg = []

    @classmethod
    def tearDownClass(cls):
        cls.oder.close()

    # 定位天线延迟配置--所配置的基站全部是在线状态
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test06001_antenna_cfg(cls):
        addr1_right = "1aa6083cf920a17"  # 正确存在的基站
        addr2_right = "1aa6083cf920913"  # 正确存在的基站
        addr3_right = "1aa6083cf91cb9d"  # 正确存在的基站
        # addr4_right = "1aa6083cf920a17"  # 正确存在的基站
        print('定位天线延迟配置:[{},{},{}]'.format(addr1_right, addr2_right, addr3_right))
        # 其中count是发送测试数据包的次数，1~65535；period是每次发送的间隔，单位毫秒ms，0~255
        instruct = '<req type="antenna cfg"><anchor addr="{}" ant_delay_rx="16492" ant_delay_tx="16492"/>' \
                   '<anchor addr="{}" ant_delay_rx="16492" ant_delay_tx="16492"/>' \
                   '<anchor addr="{}" ant_delay_rx="16492" ant_delay_tx="16492"/></req>'.format(addr1_right,
                                                                                                addr2_right,
                                                                                                addr3_right)  # 指令

        print("请求的数据：", instruct)
        cls.msg = cls.oder.yq_response(instruct)
        print("服务器返回的数据：", cls.msg)
        cls.assertNotIn('not', str(cls.msg))  # 断言响应里没有出现未连接
        print("断言'定位天线延迟配置--所配置的基站全部是在线状态'通过！")

    # 定位天线延迟配置--所配置的基站有一个离线其他全部是在线状态
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test06002_antenna_cfg1(cls):
        addr1_right = "1aa6083cf920a17"  # 正确存在的基站
        addr2_right = "1aa6083cf920913"  # 正确存在的基站
        addr3_right = "1aa6083cf91cb9d"  # 正确存在的基站
        addr4_error = "1aa6083cf920a28"  # 正确存在的基站
        print('定位天线延迟配置:离线基站:[{}]在线基站：[{},{},{}]'.format(addr4_error, addr1_right, addr2_right, addr3_right))
        # 其中count是发送测试数据包的次数，1~65535；period是每次发送的间隔，单位毫秒ms，0~255
        # 指令
        instruct = '<req type="antenna cfg"><anchor addr="{}" ant_delay_rx="16492" ant_delay_tx="16492"/>' \
                   '<anchor addr="{}" ant_delay_rx="16492" ant_delay_tx="16492"/>' \
                   '<anchor addr="{}" ant_delay_rx="16492" ant_delay_tx="16492"/>' \
                   '<anchor addr="{}" ant_delay_rx="16492" ant_delay_tx="16492"/></req>'.format(addr1_right,
                                                                                                addr2_right,
                                                                                                addr3_right,
                                                                                                addr4_error)
        print("请求的数据：", instruct)
        cls.msg = cls.oder.yq_response(instruct)
        print("服务器返回的数据：", cls.msg)
        # 断言
        cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(addr1_right),
                     str(cls.msg))  # 断言响应里该基站是已连接
        cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(addr2_right),
                     str(cls.msg))  # 断言响应里该基站是已连接
        cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(addr3_right),
                     str(cls.msg))  # 断言响应里该基站是已连接
        cls.assertIn('<anchor addr="{}" db="config saved" status="not connected"/>'.format(addr4_error),
                     str(cls.msg))  # 断言响应里该基站是未连接
        print("断言'定位天线延迟配置--所配置的基站有一个离线其他全部是在线状态'通过！")

