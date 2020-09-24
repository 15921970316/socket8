# 启用通信测试测试用例
from api.anchor_cfg import anchor_cfgs, comm_test
from api.jzyq_api import Test_api
import unittest
import time
import unit

filename = unit.BASE_DIR + "\data\engine_Data.json"
# 启用通信测试命令
class Test_comm_test(unittest.TestCase):
    status = 99

    @classmethod
    def setUpClass(cls):
        cls.oder = Test_api()
        cls.status = unit.server_state
        cls.comm_test=comm_test()
        cls.msg = []

    @classmethod
    def tearDownClass(cls):
        cls.oder.close()

    # 启用通信测试命令--所有基站都是在线状态
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test1_comm_test(cls):
        time.sleep(2)
        print("启用通信测试命令！--3基站都是在线状态")
        filename = unit.BASE_DIR + "\data\engine_Data.json"
        json1 = unit.read_name_data(filename, "comm_test1")

        cls.msg = cls.comm_test.comm_test(json1)

        a = 0
        for i in cls.msg:
            print("服务器返回的数据{}：".format(a), i)
            a += 1
        # 断言通信是否成功
        cls.assertIn('<ind type="comm test"><transmitter addr="{}"><resp status="comm test done"/>'.format(json1[0][2]),
                     str(cls.msg))  # 断言通信是否成功
        cls.assertIn('<ind type="comm test"><transmitter addr="{}"><resp status="comm test done"/>'.format(json1[0][3]),
                     str(cls.msg))  # 断言通信是否成功
        cls.assertIn('<ind type="comm test"><transmitter addr="{}"><resp status="comm test done"/>'.format(json1[0][4]),
                     str(cls.msg))  # 断言通信是否成功
        print("断言'启用通信测试命令'通过！")

    # 启用通信测试命令:--4基站全部离线状态
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test2_comm_test(cls):
        time.sleep(2)
        print("启用通信测试命令！--4基站全部离线状态")
        filename = unit.BASE_DIR + "\data\engine_Data.json"
        json1 = unit.read_name_data(filename, "comm_test2")

        cls.msg = cls.comm_test.comm_test(json1)

        a = 0
        for i in cls.msg:
            print("服务器返回的数据{}：".format(a), i)
            a += 1
        # 断言通信是否成功
        cls.assertIn('<ind type="comm test"><transmitter addr="{}"><resp status="not connected"/>'.format(json1[0][2]),
                     str(cls.msg))  # 断言通信是否成功
        cls.assertIn('<ind type="comm test"><transmitter addr="{}"><resp status="not connected"/>'.format(json1[0][3]),
                     str(cls.msg))  # 断言通信是否成功
        cls.assertIn('<ind type="comm test"><transmitter addr="{}"><resp status="not connected"/>'.format(json1[0][4]),
                     str(cls.msg))  # 断言通信是否成功
        print("断言'启用通信测试命令'通过！")

    # 启用通信测试命令: --基站3个在线状态只有一个离线状态
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test3_comm_test(cls):
        time.sleep(2)
        print("启用通信测试命令！--4个基站基站其中 前3个在线状态最后一个基站离线状态")
        filename = unit.BASE_DIR + "\data\engine_Data.json"
        json1 = unit.read_name_data(filename, "comm_test3")

        cls.msg = cls.comm_test.comm_test(json1)

        a = 0
        for i in cls.msg:
            print("服务器返回的数据{}：".format(a), i)
            a += 1
        # 断言通信是否成功
        cls.assertIn('<ind type="comm test"><transmitter addr="{}"><resp status="comm test done"/>'.format(json1[0][2]),
                     str(cls.msg))  # 断言通信是否成功
        cls.assertIn('<ind type="comm test"><transmitter addr="{}"><resp status="comm test done"/>'.format(json1[0][3]),
                     str(cls.msg))  # 断言通信是否成功
        cls.assertIn('<ind type="comm test"><transmitter addr="{}"><resp status="comm test done"/>'.format(json1[0][4]),
                     str(cls.msg))  # 断言通信是否成功
        cls.assertIn('<ind type="comm test"><transmitter addr="{}"><resp status="not connected"/>'.format(json1[0][5]),
                     str(cls.msg))  # 断言通信是否成功
        print("断言'启用通信测试命令'通过！")

