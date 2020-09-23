# 启用通信测试测试用例
from api.anchor_cfg import anchor_cfgs
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
        cls.msg = []

    @classmethod
    def tearDownClass(cls):
        cls.oder.close()

    # 启用通信测试命令--所有基站都是在线状态
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test08001_comm_test(cls):
        time.sleep(5)
        addr1_right = "1aa6083cf920a17"  # 正确存在的基站
        addr2_right = "1aa6083cf920913"  # 正确存在的基站
        addr3_right = "1aa6083cf91cb9d"  # 正确存在的基站
        print('启用通信测试命令--所有基站都是在线状态:[{},{},{}]'.format(addr1_right, addr2_right, addr3_right))
        # 其中count是发送测试数据包的次数，1~65535；period是每次发送的间隔，单位毫秒ms，0~255
        instruct = '<req type="comm test" count="100" period="10"><anchor ' \
                   'addr = "{}" />' \
                   '<anchor addr = "{}" /><anchor addr = "{}" /></req>'.format(addr1_right, addr2_right,
                                                                               addr3_right)  # 指令

        print("请求的数据：", instruct)
        cls.msg = cls.oder.yq_response2(instruct)
        print(cls.msg, '\n')
        a = 0
        for i in cls.msg:
            print("服务器返回的数据{}：".format(a), i)
            a += 1
        # 断言通信是否成功
        cls.assertIn('<ind type="comm test"><transmitter addr="{}"><resp status="comm test done"/>'.format(addr1_right),
                     str(cls.msg))  # 断言通信是否成功
        cls.assertIn('<ind type="comm test"><transmitter addr="{}"><resp status="comm test done"/>'.format(addr2_right),
                     str(cls.msg))  # 断言通信是否成功
        cls.assertIn('<ind type="comm test"><transmitter addr="{}"><resp status="comm test done"/>'.format(addr3_right),
                     str(cls.msg))  # 断言通信是否成功
        print("断言'启用通信测试命令'通过！")

    # 启用通信测试命令:--基站全部离线状态
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test08002_comm_test_error(cls):
        addr1_right = "1aa6083cf920a18"  # 正确存在的基站
        addr2_right = "1aa6083cf920914"  # 正确存在的基站
        addr3_right = "1aa6083cf91cb9e"  # 正确存在的基站
        print('启用通信测试命令--基站全部离线状态:[{},{},{}]'.format(addr1_right, addr2_right, addr3_right))
        # 其中count是发送测试数据包的次数，1~65535；period是每次发送的间隔，单位毫秒ms，0~255
        instruct = '<req type="comm test" count="100" period="10"><anchor ' \
                   'addr = "{}" />' \
                   '<anchor addr = "{}" /></req>'.format(addr1_right, addr2_right, addr3_right)  # 指令

        # duration是次序发送连续帧的时长 单位秒
        print("请求的数据：", instruct)
        cls.msg = cls.oder.yq_response2(instruct)

        a = 0
        for i in cls.msg:
            print("服务器返回的数据{}：".format(a), i)
            a += 1

        cls.assertNotIn('status="comm test done"', str(cls.msg))  # 断言响应里没有成功的状态
        print("断言'启用通信测试命令'通过！")

    # 启用通信测试命令: --基站3个在线状态只有一个离线状态
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test08003_comm_test_error(cls):

        addr_error = "1aa6083cf920914"
        addr1 = "1aa6083cf91cb9d"
        addr2 = "1aa6083cf920a17"
        addr3 = "1aa6083cf920913"
        print('启用通信测试命令:--基站三个在线状态[{},{},{}]一个离线状态[{}]'.format(addr1, addr2, addr3, addr_error))

        instruct = '<req type="comm test" count="100" period="10">' \
                   '<anchor addr = "{}" /><anchor addr = "{}" />' \
                   '<anchor addr = "{}" /><anchor addr = "{}" /></req>'.format(addr1, addr2, addr3, addr_error)  # 指令

        print("请求的数据：", instruct)
        cls.msg = cls.oder.yq_response2(instruct)

        a = 0
        for i in cls.msg:
            print("服务器返回的数据{}：".format(a), i)
            a += 1
        # 断言通信是否成功
        cls.assertIn('<ind type="comm test"><transmitter addr="{}"><resp status="comm test done"/>'.format(addr1),
                     str(cls.msg))  # 断言通信离线基站连接成功的状态
        cls.assertIn('<ind type="comm test"><transmitter addr="{}"><resp status="comm test done"/>'.format(addr2),
                     str(cls.msg))  # 断言通信离线基站连接成功的状态
        cls.assertIn('<ind type="comm test"><transmitter addr="{}"><resp status="comm test done"/>'.format(addr3),
                     str(cls.msg))  # 断言通信离线基站连接成功的状态
        cls.assertIn('<ind type="comm test"><transmitter addr="{}"><resp status="not connected"/>'.format(addr_error),
                     str(cls.msg))  # 断言通信离线基站连接未成功的状态
        print("断言启用通信测试命令:--基站三个在线状态[{},{},{}]一个离线状态[{}]状态全部通过".format(addr1, addr2, addr3, addr_error))

