# 启用功率测试用例
from api.anchor_cfg import anchor_cfgs
from api.jzyq_api import Test_api
import unittest
import time
import unit

filename = unit.BASE_DIR + "\data\engine_Data.json"
# 启用功率测试
class Test_power_test(unittest.TestCase):
    status = 99

    @classmethod
    def setUpClass(cls):
        cls.oder = Test_api()
        cls.status = unit.server_state
        cls.msg = []

    @classmethod
    def tearDownClass(cls):
        cls.oder.close()

    # 启用功率测试--基站全部正常在线
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test09001_power_test(cls):
        addr1 = '1aa6083cf920a17'  # 在线基站
        addr2 = '1aa6083cf920913'  # 在线基站
        addr3 = '1aa6083cf91cb9d'  # 在线基站
        print('启用功率测试:--基站全部正常在线[{},{},{}]'.format(addr1, addr2, addr3))
        instruct = '<req type="power test" duration="1">' \
                   '<anchor addr = "{}" /><anchor addr = "{}" />' \
                   '<anchor addr = "{}" /></req>'.format(addr1, addr2, addr3)  # 指令
        # duration是次序发送连续帧的时长 单位秒
        print("请求的数据：", instruct)
        cls.msg = cls.oder.yq_response3(instruct)
        a = 0
        for i in cls.msg:
            print("服务器返回的数据{}：".format(a), i)
            a += 1
        # 断言
        cls.assertIn('<ind type="power test" addr="{}" status="power test done"/></ind>'.format(addr1),
                     str(cls.msg))  # 断言
        print("断言'启用功率测试--在线的基站{}测试'通过！".format(addr1))
        cls.assertIn('<ind type="power test" addr="{}" status="power test done"/></ind>'.format(addr2),
                     str(cls.msg))  # 断言
        print("断言'启用功率测试--在线的基站{}测试'通过！".format(addr2))
        cls.assertIn('<ind type="power test" addr="{}" status="power test done"/></ind>'.format(addr3),
                     str(cls.msg))  # 断言
        print("断言'启用功率测试--在线的基站{}测试'通过！".format(addr3))

    # 启用功率测试--基站adrr有一个基站在线，其他基站离线和字符长度错误基站时
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test09002_power_test_error1(cls):
        addr = '1aa6083cf920a17'  # 在线基站

        addr_error1 = '1aa6083cf920a18'  # 离线基站
        addr_error2 = '1aa6083c'  # 8位的16进制字符基站
        addr_error3 = '1afa6083cf91cb9ebcdefab'  # 17位16进制的字符基站
        addr_error4 = '1aax6083c'  # 超出16进制字符标准的基站
        print('启用功率测试-0-基站adrr[{}]有一个在线，2个基站[{},{}]出现字符长度错误、一个含有超出字母a到F的字符的基站addr：[{}]、一个[{}]离线时:'.format(addr,
                                                                                                          addr_error2,
                                                                                                          addr_error3,
                                                                                                          addr_error1,
                                                                                                          addr_error4))
        instruct = '<req type="power test" duration="1">' \
                   '<anchor addr="{}" />' \
                   '<anchor addr = "{}" />' \
                   '<anchor addr = "{}" />' \
                   '<anchor addr = "{}" />' \
                   '<anchor addr = "{}" /></req>'.format(addr, addr_error1, addr_error2, addr_error3, addr_error4)  # 指令
        print("请求的数据：", instruct)
        cls.msg = cls.oder.yq_response3(instruct)
        a = 0
        for i in cls.msg:
            print("服务器返回的数据{}：".format(a), i)
            a += 1
        cls.assertIn('<ind type="power test" addr="{}" status="power test done"/></ind>'.format(addr),
                     str(cls.msg))  # 断言
        print("断言'启用功率测试--在线的基站{}测试'通过！".format(addr))
        cls.assertIn('<ind type="power test" addr="{}" status="not connected"/></ind>'.format(addr_error1),
                     str(cls.msg))  # 断言
        print("断言'启用功率测试--离线的基站{}测试'通过！".format(addr_error1))
        cls.assertIn('<ind type="power test" addr="{}" status="not connected"/></ind>'.format(addr_error2),
                     str(cls.msg))  # 断言
        print("断言'启用功率测试--离线的基站{}测试'通过！".format(addr_error2))
        cls.assertIn('<ind type="power test" addr="{}" status="not connected"/></ind>'.format(addr_error3),
                     str(cls.msg))  # 断言
        print("断言'启用功率测试--离线的基站{}测试'通过！".format(addr_error3))

    # 启用功率测试--基站adrr全部出现错误或者离线时
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test09003_power_test_error2(cls):
        addr1 = "1aa6083cf920a19"
        addr2 = "1aa6083cf920914"
        addr3 = "1aa6083cf91cb9e"
        print('启用功率测试--基站adrr全部出现错误或者离线时:')
        instruct = '<req type="power test" duration="10">' \
                   '<anchor addr = "{}" />' \
                   '<anchor addr = "{}" />' \
                   '<anchor addr = "{}" /></req>'.format(addr1, addr2, addr3)  # 指令

        cls.msg = cls.oder.yq_response3_error(instruct)
        a = 0
        for i in cls.msg:
            print("服务器返回的数据{}：".format(a), i)
            a += 1

        cls.assertIn('status="not connected"', str(cls.msg))  # 断言
        print("断言'启用功率测试--基站adrr出现错误或者离线时'通过！")
