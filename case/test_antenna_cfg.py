#定位天线延迟配置 测试用例
from api.anchor_cfg import antenna_cfg
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

        cls.antenna_cfg1=antenna_cfg()
    @classmethod
    def tearDownClass(cls):
        cls.oder.close()

    # 定位天线延迟配置--所配置正常
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test1_antenna_cfg(cls):
        filename = unit.BASE_DIR + "\data\engine_Data.json"
        json1 = unit.read_name_data(filename, "antenna_cfg1")
        cls.msg = cls.antenna_cfg1.antenna_cfg(json1)
        print("服务器返回的数据：", cls.msg)
        # 断言
        cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(json1[0][0]),
                     str(cls.msg))  # 断言响应里该基站addr
        print("断言'定位天线延迟配置--所配置的基站全部是在线状态'通过！")

    # 定位天线延迟配置--接收配置为0
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test2_antenna_cfg1(cls):
        filename = unit.BASE_DIR + "\data\engine_Data.json"
        json1 = unit.read_name_data(filename, "antenna_cfg2")
        cls.msg = cls.antenna_cfg1.antenna_cfg(json1)
        print("服务器返回的数据：", cls.msg)
        # 断言
        cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(json1[0][0]),
                     str(cls.msg))  # 断言响应里该基站addr


        print("断言'定位天线延迟配置--所配置的基站有一个离线其他全部是在线状态'通过！")

    # 定位天线延迟配置--接收配置为-1
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test3_antenna_cfg3(cls):
        filename = unit.BASE_DIR + "\data\engine_Data.json"
        json1 = unit.read_name_data(filename, "antenna_cfg3")
        cls.msg = cls.antenna_cfg1.antenna_cfg(json1)
        print("服务器返回的数据：", cls.msg)
        # 断言
        cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(json1[0][0]),
                     str(cls.msg))  # 断言响应里该基站addr

        print("断言'定位天线延迟配置--所配置的基站有一个离线其他全部是在线状态'通过！")

    # 定位天线延迟配置--接收配置为65536
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test4_antenna_cfg4(cls):
        filename = unit.BASE_DIR + "\data\engine_Data.json"
        json1 = unit.read_name_data(filename, "antenna_cfg4")
        cls.msg = cls.antenna_cfg1.antenna_cfg(json1)
        print("服务器返回的数据：", cls.msg)
        # 断言
        cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(json1[0][0]),
                     str(cls.msg))  # 断言响应里该基站addr
        # cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(json1[0][1]),
        #              str(cls.msg))  # 断言响应里该基站接收天线延迟ant_delay_rx
        # cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(json1[0][2]),
        #              str(cls.msg))  # 断言响应里该基站发射天线延迟ant_delay_tx

        print("断言'定位天线延迟配置--所配置的基站有一个离线其他全部是在线状态'通过！")

    # 定位天线延迟配置--发射配置为65536
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test5_antenna_cfg5(cls):
        filename = unit.BASE_DIR + "\data\engine_Data.json"
        json1 = unit.read_name_data(filename, "antenna_cfg5")
        cls.msg = cls.antenna_cfg1.antenna_cfg(json1)
        print("服务器返回的数据：", cls.msg)
        # 断言
        cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(json1[0][0]),
                     str(cls.msg))  # 断言响应里该基站addr
        # cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(json1[0][1]),
        #              str(cls.msg))  # 断言响应里该基站接收天线延迟ant_delay_rx
        # cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(json1[0][2]),
        #              str(cls.msg))  # 断言响应里该基站发射天线延迟ant_delay_tx

        print("断言'定位天线延迟配置--所配置的基站有一个离线其他全部是在线状态'通过！")

    # 定位天线延迟配置--发射配置为-1
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test6_antenna_cfg6(cls):
        filename = unit.BASE_DIR + "\data\engine_Data.json"
        json1 = unit.read_name_data(filename, "antenna_cfg6")
        cls.msg = cls.antenna_cfg1.antenna_cfg(json1)
        print("服务器返回的数据：", cls.msg)
        # 断言
        cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(json1[0][0]),
                     str(cls.msg))  # 断言响应里该基站addr
        # cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(json1[0][1]),
        #              str(cls.msg))  # 断言响应里该基站接收天线延迟ant_delay_rx
        # cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(json1[0][2]),
        #              str(cls.msg))  # 断言响应里该基站发射天线延迟ant_delay_tx

        print("断言'定位天线延迟配置--所配置的基站有一个离线其他全部是在线状态'通过！")

    # 定位天线延迟配置--发射配置为65535
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test7_antenna_cfg7(cls):
        filename = unit.BASE_DIR + "\data\engine_Data.json"
        json1 = unit.read_name_data(filename, "antenna_cfg7")
        cls.msg = cls.antenna_cfg1.antenna_cfg(json1)
        print("服务器返回的数据：", cls.msg)
        # 断言
        cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(json1[0][0]),
                     str(cls.msg))  # 断言响应里该基站addr
        # cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(json1[0][1]),
        #              str(cls.msg))  # 断言响应里该基站接收天线延迟ant_delay_rx
        # cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(json1[0][2]),
        #              str(cls.msg))  # 断言响应里该基站发射天线延迟ant_delay_tx

        print("断言'定位天线延迟配置--所配置的基站有一个离线其他全部是在线状态'通过！")

