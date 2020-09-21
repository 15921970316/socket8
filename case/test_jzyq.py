# 测试用例
from api.anchor_cfg import anchor_cfgs
from api.jzyq_api import Test_api
import unittest
import time
import unit

filename = unit.BASE_DIR + "\data\engine_Data.json"


# 基站配置
class Test_anchor_cfg(unittest.TestCase):
    status = 99

    @classmethod
    def setUpClass(cls):
        cls.oder = Test_api()
        cls.status = unit.server_state
        cls.msg = []


        cls.anchor_cfg1=anchor_cfgs()



    @classmethod
    def tearDownClass(cls):
        cls.oder.close()
    # 对3个在线1个离线的基站进行配置
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test01001_anchor_cfg(cls):
        print('对4个在线的基站进行配置')
        filename = unit.BASE_DIR + "\data\engine_Data.json"
        print("filename的路径为：", filename)
        json1 = unit.read_name_data(filename, "data1")
        json2 = unit.read_name_data(filename, "data2")
        json3 = unit.read_name_data(filename, "data3")
        json4 = unit.read_name_data(filename, "data4")
        cls.msg = cls.anchor_cfg1.anchor_cfg(json1, json2, json3, json4)
        print("服务器返回的数据：", str(cls.msg, 'utf8'))
        cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(json1[0][0]),
                     str(cls.msg, 'utf8'))
        print("断言'{}'通过！".format(json1[0][0]))
        cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(json2[0][0]),
                     str(cls.msg, 'utf8'))
        print("断言'{}'通过！".format(json2[0][0]))
        cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(json3[0][0]),
                     str(cls.msg, 'utf8'))
        print("断言'{}'通过！".format(json3[0][0]))
        cls.assertIn('<anchor addr="{}" db="config saved" status="not connected"/>'.format(json4[0][0]),
                     str(cls.msg, 'utf8'))
        print("断言'{}'通过！".format(json4[0][0]))
    # 对单个基站进行配置
    def test01002_anchor_cfg(cls):
        print('对单个在线的基站进行配置')
        filename = unit.BASE_DIR + "\data\engine_Data.json"
        json1 = unit.read_name_data(filename, "data1")
        cls.msg = cls.anchor_cfg1.anchor_cfg_one(json1)
        print("服务器返回的数据：", str(cls.msg, 'utf8'))
        cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(json1[0][0]),
                     str(cls.msg, 'utf8'))
        print("断言'{}'配置通过！".format(json1[0][0]))

    # # 对有不在线基站进行配置
    # @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    # def test01002_anchor_cfg_Error(cls):
    #     addr1_right = "1aa6083cf920a17"  # 正确存在的基站
    #     addr2_Error = "1aa6083cf920914"  # 错误或者不存在的基站
    #     addr3_Error = "2aa6085cf92a81a"  # 错误或者不存在的基站
    #     addr4_Error = "1aa6083cf92080b"  # 错误或者不存在的基站
    #     print('对不在线的基站{},{},{}和在线的基站{}的同时进行配置命令!'.format(addr2_Error, addr3_Error, addr4_Error, addr1_right))
    #     # 指令
    #     instruct = '<req type="anchor cfg"><anchor addr="{}" x="1.30" y="2.27" z="2.52" syncref="1" ' \
    #                'follow_addr="0" lag_delay="0"></anchor>' \
    #                '<anchor addr="{}" x="7.93" y="0.87" z="2.53" syncref="0" follow_addr="0" lag_delay="0">' \
    #                '<syncrefanchor addr="{}" rfdistance="0"/></anchor>' \
    #                '<anchor addr="{}" x="7.93" y="0.87" z="2.53" syncref="0" follow_addr="0" lag_delay="0">' \
    #                '<syncrefanchor addr="{}" rfdistance="0"/></anchor>' \
    #                '<anchor addr="{}" x="8.04" y="10.43" z="2.56" ' \
    #                'syncref="0" follow_addr="0" lag_delay="0"><syncrefanchor addr="{}" rfdistance="0"/></anchor>' \
    #                '</req>'' '.format(addr1_right, addr2_Error, addr1_right, addr3_Error, addr1_right, addr4_Error,
    #                                   addr1_right)
    #
    #     print("请求的数据：", instruct)
    #
    #     cls.msg = cls.oder.yq_response(instruct)
    #     # 断言配置设置成功标识符
    #     print("服务器返回的数据：", str(cls.msg, 'utf8'))
    #     cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(addr1_right),
    #                  str(cls.msg, 'utf8'))
    #     print("断言'{}'通过！".format(addr1_right))
    #     cls.assertIn('<anchor addr="{}" db="config saved" status="not connected"/>'.format(addr2_Error),
    #                  str(cls.msg, 'utf8'))
    #     print("断言'{}'通过！".format(addr2_Error))
    #     cls.assertIn('<anchor addr="{}" db="config saved" status="not connected"/>'.format(addr3_Error),
    #                  str(cls.msg, 'utf8'))
    #     print("断言'{}'通过！".format(addr3_Error))
    #     cls.assertIn('<anchor addr="{}" db="config saved" status="not connected"/>'.format(addr4_Error),
    #                  str(cls.msg, 'utf8'))
    #     print("断言'{}'通过！".format(addr4_Error))
    #
    # # 对在线的基站进行配置
    # @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    # def test01001_anchor_cfg(cls):
    #     json = unit.read_name_data(filename, "data")
    #
    #     # filename = app.BASE_DIR + "/data/login_data.json"
    #     # print("filename的路径为：", filename)
    #     # read_login_data(filename)
    #     print('对在线的基站进行配置命令:')
    #     print(cls.status)
    #     addr1_right = "1aa6083cf920a17"  # 正确存在的基站
    #     addr2_right = "1aa6083cf920913"  # 正确存在的基站
    #     addr3_right = "1aa6083cf91cb9d"  # 正确存在的基站
    #     # addr4_right = "1aa6083cf920a17"  # 正确存在的基站
    #     # 指令
    #     instruct = '<req type="anchor cfg"><anchor addr="{}" x="1.30" y="2.27" z="2.52" syncref="1" ' \
    #                'follow_addr="0" lag_delay="0"></anchor>' \
    #                '<anchor addr="{}" x="7.93" y="0.87" z="2.53" syncref="0" follow_addr="0" lag_delay="0">' \
    #                '<syncrefanchor addr="{}" rfdistance="0"/></anchor>' \
    #                '<anchor addr="{}" x="8.04" y="10.43" z="2.56" ' \
    #                'syncref="0" follow_addr="0" lag_delay="0"><syncrefanchor addr="{}" rfdistance="0"/></anchor></req>'' '.format(
    #         addr1_right, addr2_right, addr1_right, addr3_right, addr1_right)
    #
    #     print("请求的数据：", instruct)
    #     cls.msg = cls.oder.yq_response(instruct)
    #     # 断言配置设置未成功标识符status="not connected"已配置
    #
    #     print("服务器返回的数据：", str(cls.msg, 'utf8'))
    #     cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(addr1_right),
    #                  str(cls.msg, 'utf8'))
    #     print("断言'{}'通过！".format(addr1_right))
    #     cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(addr2_right),
    #                  str(cls.msg, 'utf8'))
    #     print("断言'{}'通过！".format(addr2_right))
    #     cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(addr3_right),
    #                  str(cls.msg, 'utf8'))
    #     print("断言'{}'通过！".format(addr3_right))
    #
    # # 对有不在线基站进行配置--不在线的基站作为时间同步基站
    # @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    # def test01003_anchor_cfg_Error(cls):
    #     addr1_right = "1aa6083cf920a17"  # 正确存在的基站
    #     addr2_Error = "1aa6083cf920914"  # 错误或者不存在的基站 作为时间同步基站
    #     addr3_Error = "2aa6085cf92a81a"  # 错误或者不存在的基站
    #     addr4_Error = "1aa6083cf92080b"  # 错误或者不存在的基站
    #     print(
    #         '对不在线的基站--时间同步基站：[{}],{},{}和在线的基站{}的同时进行配置命令!--不在线的基站作为时间同步基站'.format(addr2_Error, addr3_Error, addr4_Error,
    #                                                                               addr1_right))
    #     # 指令
    #     instruct = '<req type="anchor cfg"><anchor addr="{}" x="1.30" y="2.27" z="2.52" syncref="1" ' \
    #                'follow_addr="0" lag_delay="0"></anchor>' \
    #                '<anchor addr="{}" x="7.93" y="0.87" z="2.53" syncref="0" follow_addr="0" lag_delay="0">' \
    #                '<syncrefanchor addr="{}" rfdistance="0"/></anchor>' \
    #                '<anchor addr="{}" x="7.93" y="0.87" z="2.53" syncref="0" follow_addr="0" lag_delay="0">' \
    #                '<syncrefanchor addr="{}" rfdistance="0"/></anchor>' \
    #                '<anchor addr="{}" x="8.04" y="10.43" z="2.56" ' \
    #                'syncref="0" follow_addr="0" lag_delay="0"><syncrefanchor addr="{}" rfdistance="0"/></anchor>' \
    #                '</req>'' '.format(addr2_Error, addr1_right, addr2_Error, addr3_Error, addr2_Error, addr4_Error,
    #                                   addr2_Error)
    #
    #     print("请求的数据：", instruct)
    #
    #     cls.msg = cls.oder.yq_response(instruct)
    #     # 断言配置设置成功标识符
    #     print("服务器返回的数据：", str(cls.msg, 'utf8'))
    #     cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(addr1_right),
    #                  str(cls.msg, 'utf8'))
    #     print("断言'{}'通过！".format(addr1_right))
    #     cls.assertIn('<anchor addr="{}" db="config saved" status="not connected"/>'.format(addr2_Error),
    #                  str(cls.msg, 'utf8'))
    #     print("断言'{}'通过！".format(addr2_Error))
    #     cls.assertIn('<anchor addr="{}" db="config saved" status="not connected"/>'.format(addr3_Error),
    #                  str(cls.msg, 'utf8'))
    #     print("断言'{}'通过！".format(addr3_Error))
    #     cls.assertIn('<anchor addr="{}" db="config saved" status="not connected"/>'.format(addr4_Error),
    #                  str(cls.msg, 'utf8'))
    #     print("断言'{}'通过！".format(addr4_Error))
    #
    # # 对addr为空的基站进行配置
    # @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    # def test01004_anchor_cfg(cls):
    #     print('对addr为空的基站进行配置命令:')
    #     print(cls.status)
    #     addr = ''
    #     addr1_right = "1aa6083cf920a17"  # 正确存在的基站
    #     addr2_right = "1aa6083cf920913"  # 正确存在的基站
    #     addr3_right = "1aa6083cf91cb9d"  # 正确存在的基站
    #     # addr4_right = "1aa6083cf920a17"  # 正确存在的基站
    #     # 指令
    #     instruct = '<req type="anchor cfg"><anchor addr="{}" ' \
    #                'x="1.30" y="2.27" z="2.52" syncref="0" ' \
    #                'follow_addr="0" lag_delay="0"></anchor></req>'.format(addr)
    #
    #     print("请求的数据：", instruct)
    #     cls.msg = cls.oder.yq_response(instruct)
    #     # 断言配置设置未成功标识符status="not connected"已配置
    #
    #     print("服务器返回的数据：", str(cls.msg, 'utf8'))
    #     cls.assertIn('<anchor addr="{}" db="config saved" status="not connected"/>'.format(addr), str(cls.msg, 'utf8'))


# # 查询基站列表
# class Test_anchor_list(unittest.TestCase):
#     print('查询基站列表')
#     status = 99
#
#     @classmethod
#     def setUpClass(cls):
#         cls.oder = Test_api()
#         cls.status = unit.server_state
#         cls.msg = []
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.oder.close()
#
#     # 查询基站列表
#     @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
#     def test02001_anchor_list(cls):
#         addr1_right = "1aa6083cf920a17"  # 正确存在的基站
#         addr2_right = "1aa6083cf920913"  # 正确存在的基站
#         addr3_right = "1aa6083cf91cb9d"  # 正确存在的基站
#         print('查询基站列表:')
#         instruct = '<req type="anchor list"/>'  # 指令
#         print('请求的数据：{}'.format(instruct))
#         cls.msg = cls.oder.yq_response(instruct)
#         cls.assertIn('<ind type="anchor list">', str(cls.msg, 'utf8'))
#         print("\n服务器返回的数据：", str(cls.msg, 'utf8'))
#         #
#         # 断言响应
#         cls.assertIn('addr="{}"'.format(addr1_right), str(cls.msg, 'utf8'))
#         cls.assertIn('addr="{}"'.format(addr2_right), str(cls.msg, 'utf8'))
#         cls.assertIn('addr="{}"'.format(addr3_right), str(cls.msg, 'utf8'))
#         print("断言'基站查询'通过！")
#
#     # 对查询基站列表指令进行1000次重复
#     @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
#     def test02002_anchor_list(cls):
#         count = 1000
#         i = 1
#         print('即将进行10000次的查询基站列表:')
#         print('请求的数据：<req type="anchor list"/>')
#         while i <= count:
#             instruct = '<req type="anchor list"/>'  # 指令
#
#             cls.msg = cls.oder.yq_response(instruct)
#
#             print("\n服务器第{}次返回的数据：".format(i), str(cls.msg, 'utf8'))
#             cls.assertIn('<ind type="anchor list">', str(cls.msg, 'utf8'))
#             print("断言'基站查询'通过！{}".format(i))
#             i += 1
#
#
# # 设置定位算法参数
# class Test_multilateration(unittest.TestCase):
#     status = 99
#
#     @classmethod
#     def setUpClass(cls):
#         cls.oder = Test_api()
#         cls.status = unit.server_state
#         cls.msg = []
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.oder.close()
#
#     # 定位算法配置命令
#     @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
#     def test03001_anchor_multilateration(cls):
#         print('定位算法配置命令:')
#         # 指令
#         instruct = '<req type="multilateration" algorithm="3"/>'
#         print("请求的数据：", instruct)
#         cls.msg = cls.oder.yq_response(instruct)
#         print("服务器返回的数据：", str(cls.msg, 'utf8'))
#         # 断言响应
#         cls.assertIn('<ind type="multilateration"/>', str(cls.msg, 'utf8'))
#         print("断言'定位算法配置命令'通过！")
#
#
# # 双向测距
# class Test_ranging_test(unittest.TestCase):
#     status = 99
#
#     @classmethod
#     def setUpClass(cls):
#         cls.oder = Test_api()
#         cls.status = unit.server_state
#         cls.msg = []
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.oder.close()
#
#     ## 双向测距
#     @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
#     def test04001_ranging_test(cls):
#         addr1_right = "1aa6083cf920a17"  # 正确存在的基站
#         addr2_right = "1aa6083cf920913"  # 正确存在的基站
#         addr3_right = "1aa6083cf91cb9d"  # 正确存在的基站
#         # addr4_right = "1aa6083cf920a17"  # 正确存在的基站
#         print('双向测距:[{},{},{}]'.format(addr1_right, addr2_right, addr3_right))
#         instruct = '<req type="range test" num_ranges="100" res_delay="" fin_delay="" reverse="1">' \
#                    '<anchor addr = "{}"/><anchor addr = "{}"/>' \
#                    '<anchor addr = "{}"/> </req>'.format(addr1_right, addr2_right, addr3_right)
#         print("请求的数据：", instruct)
#         cls.msg = cls.oder.yq_response2(instruct)
#         a = 0
#         for i in cls.msg:
#             print("服务器返回的数据{}：".format(a), i)
#             a += 1
#         # 断言响应
#         cls.assertIn('<ind type="system status" msg="range measurement completes"></ind>', str(cls.msg))
#         print("断言'双向测距'通过！")
#
#
# # 启、停定位
# class Test_rtls_start_stop(unittest.TestCase):
#     status = 99
#
#     @classmethod
#     def setUpClass(cls):
#         cls.oder = Test_api()
#         cls.status = unit.server_state
#         cls.msg = []
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.oder.close()
#
#     # 开始定位
#     @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
#     def test05001_start_positioning(cls):
#         print('开始定位:')
#         instruct = '<req type="rtls start"></req>'  # 指令
#         print("请求的数据：", instruct)
#         cls.msg = cls.oder.yq_response(instruct)
#
#         print("服务器返回的数据：", str(cls.msg, 'utf8'))
#         time.sleep(10)
#         cls.assertIn('<ind type="rtls start"/>', str(cls.msg, 'utf8'))  # 断言
#         print("断言'开始定位'通过！")
#
#     # 停止定位
#     @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
#     def test05003_Stop_positioning(cls):
#         try:
#             print('停止定位:')
#             instruct = '<req type="rtls stop"/>'  # 指令
#             print("请求的数据：", instruct)
#             cls.msg = cls.oder.yq_response(instruct)
#
#             print("服务器返回的数据：", str(cls.msg, 'utf8'))
#
#             cls.assertIn('<ind type="rtls stop"/>', str(cls.msg, 'utf8'))  # 断言
#             print("断言'停止定位'通过！")
#         except Exception as e:
#             print(e)
#
#         # 停止定位后查询定位状态
#
#
# # 定位状态
# class Test_rtls_status(unittest.TestCase):
#     status = 99
#
#     @classmethod
#     def setUpClass(cls):
#         cls.oder = Test_api()
#         cls.status = unit.server_state
#         cls.msg = []
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.oder.close()
#
#     # 开始定位后查询定位状态
#     @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
#     def test05002_rtls_start_status(cls):
#         print('开始定位:')
#         instruct = '<req type="rtls start"></req>'  # 指令
#         print("请求的数据：", instruct)
#         cls.msg = cls.oder.yq_response(instruct)
#
#         print("服务器返回的数据：", str(cls.msg, 'utf8'))
#         time.sleep(10)
#         cls.assertIn('<ind type="rtls start"/>', str(cls.msg, 'utf8'))  # 断言
#         print("断言'开始定位'通过！")
#         print('开始定位后查询定位状态:')
#         instruct = '<req type="rtls state"/>'  # 指令
#         print("请求的数据：", instruct)
#         cls.msg = cls.oder.yq_response(instruct)
#
#         print("服务器返回的数据：", str(cls.msg, 'utf8'))
#         time.sleep(10)
#         cls.assertIn('<ind type="rtls state" state="running"/>', str(cls.msg, 'utf8'))  # 断言
#         print("断言'开始定位后查询定位状态'通过！")
#
#     # 停止定位后查询定位状态
#     @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
#     def test05004_rtls_stop_start(cls):
#         try:
#             print('停止定位:')
#             instruct = '<req type="rtls stop"/>'  # 指令
#             print("请求的数据：", instruct)
#             cls.msg = cls.oder.yq_response(instruct)
#
#             print("服务器返回的数据：", str(cls.msg, 'utf8'))
#
#             cls.assertIn('<ind type="rtls stop"/>', str(cls.msg, 'utf8'))  # 断言
#             print("断言'停止定位'通过！")
#         except Exception as e:
#             print(e)
#         print('停止定位后查询定位状态:')
#         instruct = '<req type="rtls state"/>'  # 指令
#         print("请求的数据：", instruct)
#         cls.msg = cls.oder.yq_response(instruct)
#
#         print("服务器返回的数据：", str(cls.msg, 'utf8'))
#
#         cls.assertIn('<ind type="rtls state" state="stopped"/>', str(cls.msg, 'utf8'))  # 断言
#         print("断言'停止定位后查询定位状态'通过！")
#
#
# # 定位天线延迟配置
# class Test_antenna_cfg(unittest.TestCase):
#     status = 99
#
#     @classmethod
#     def setUpClass(cls):
#         cls.oder = Test_api()
#         cls.status = unit.server_state
#         cls.msg = []
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.oder.close()
#
#     # 定位天线延迟配置--所配置的基站全部是在线状态
#     @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
#     def test06001_antenna_cfg(cls):
#         addr1_right = "1aa6083cf920a17"  # 正确存在的基站
#         addr2_right = "1aa6083cf920913"  # 正确存在的基站
#         addr3_right = "1aa6083cf91cb9d"  # 正确存在的基站
#         # addr4_right = "1aa6083cf920a17"  # 正确存在的基站
#         print('定位天线延迟配置:[{},{},{}]'.format(addr1_right, addr2_right, addr3_right))
#         # 其中count是发送测试数据包的次数，1~65535；period是每次发送的间隔，单位毫秒ms，0~255
#         instruct = '<req type="antenna cfg"><anchor addr="{}" ant_delay_rx="16492" ant_delay_tx="16492"/>' \
#                    '<anchor addr="{}" ant_delay_rx="16492" ant_delay_tx="16492"/>' \
#                    '<anchor addr="{}" ant_delay_rx="16492" ant_delay_tx="16492"/></req>'.format(addr1_right,
#                                                                                                 addr2_right,
#                                                                                                 addr3_right)  # 指令
#
#         print("请求的数据：", instruct)
#         cls.msg = cls.oder.yq_response(instruct)
#         print("服务器返回的数据：", cls.msg)
#         cls.assertNotIn('not', str(cls.msg))  # 断言响应里没有出现未连接
#         print("断言'定位天线延迟配置--所配置的基站全部是在线状态'通过！")
#
#     # 定位天线延迟配置--所配置的基站有一个离线其他全部是在线状态
#     @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
#     def test06002_antenna_cfg1(cls):
#         addr1_right = "1aa6083cf920a17"  # 正确存在的基站
#         addr2_right = "1aa6083cf920913"  # 正确存在的基站
#         addr3_right = "1aa6083cf91cb9d"  # 正确存在的基站
#         addr4_error = "1aa6083cf920a28"  # 正确存在的基站
#         print('定位天线延迟配置:离线基站:[{}]在线基站：[{},{},{}]'.format(addr4_error, addr1_right, addr2_right, addr3_right))
#         # 其中count是发送测试数据包的次数，1~65535；period是每次发送的间隔，单位毫秒ms，0~255
#         # 指令
#         instruct = '<req type="antenna cfg"><anchor addr="{}" ant_delay_rx="16492" ant_delay_tx="16492"/>' \
#                    '<anchor addr="{}" ant_delay_rx="16492" ant_delay_tx="16492"/>' \
#                    '<anchor addr="{}" ant_delay_rx="16492" ant_delay_tx="16492"/>' \
#                    '<anchor addr="{}" ant_delay_rx="16492" ant_delay_tx="16492"/></req>'.format(addr1_right,
#                                                                                                 addr2_right,
#                                                                                                 addr3_right,
#                                                                                                 addr4_error)
#         print("请求的数据：", instruct)
#         cls.msg = cls.oder.yq_response(instruct)
#         print("服务器返回的数据：", cls.msg)
#         # 断言
#         cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(addr1_right),
#                      str(cls.msg))  # 断言响应里该基站是已连接
#         cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(addr2_right),
#                      str(cls.msg))  # 断言响应里该基站是已连接
#         cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(addr3_right),
#                      str(cls.msg))  # 断言响应里该基站是已连接
#         cls.assertIn('<anchor addr="{}" db="config saved" status="not connected"/>'.format(addr4_error),
#                      str(cls.msg))  # 断言响应里该基站是未连接
#         print("断言'定位天线延迟配置--所配置的基站有一个离线其他全部是在线状态'通过！")
#
#
# # 射频配置命令
# class Test_rf_cfg(unittest.TestCase):
#     status = 99
#
#     @classmethod
#     def setUpClass(cls):
#         cls.oder = Test_api()
#         cls.status = unit.server_state
#         cls.msg = []
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.oder.close()
#
#     # 射频配置命令
#     @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
#     def test07001_rf_cfg(cls):
#         print('射频配置命令:')
#         # 其中count是发送测试数据包的次数，1~65535；period是每次发送的间隔，单位毫秒ms，0~255
#         instruct = '<req type="rf cfg"><rf chan="2" prf="64" rate="6810" code="9" plen="128" pac="8" nsfd="0"/></req>'  # 指令
#
#         print("请求的数据：", instruct)
#         cls.msg = cls.oder.yq_response(instruct)
#
#         print("服务器返回的数据：", cls.msg)
#         cls.assertIn('status="config sent"', str(cls.msg))  # 断言
#         print("断言'射频配置命令'通过！")
#
#
# # 启用通信测试命令
# class Test_comm_test(unittest.TestCase):
#     status = 99
#
#     @classmethod
#     def setUpClass(cls):
#         cls.oder = Test_api()
#         cls.status = unit.server_state
#         cls.msg = []
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.oder.close()
#
#     # 启用通信测试命令--所有基站都是在线状态
#     @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
#     def test08001_comm_test(cls):
#         time.sleep(5)
#         addr1_right = "1aa6083cf920a17"  # 正确存在的基站
#         addr2_right = "1aa6083cf920913"  # 正确存在的基站
#         addr3_right = "1aa6083cf91cb9d"  # 正确存在的基站
#         print('启用通信测试命令--所有基站都是在线状态:[{},{},{}]'.format(addr1_right, addr2_right, addr3_right))
#         # 其中count是发送测试数据包的次数，1~65535；period是每次发送的间隔，单位毫秒ms，0~255
#         instruct = '<req type="comm test" count="100" period="10"><anchor ' \
#                    'addr = "{}" />' \
#                    '<anchor addr = "{}" /><anchor addr = "{}" /></req>'.format(addr1_right, addr2_right,
#                                                                                addr3_right)  # 指令
#
#         print("请求的数据：", instruct)
#         cls.msg = cls.oder.yq_response2(instruct)
#         print(cls.msg, '\n')
#         a = 0
#         for i in cls.msg:
#             print("服务器返回的数据{}：".format(a), i)
#             a += 1
#         # 断言通信是否成功
#         cls.assertIn('<ind type="comm test"><transmitter addr="{}"><resp status="comm test done"/>'.format(addr1_right),
#                      str(cls.msg))  # 断言通信是否成功
#         cls.assertIn('<ind type="comm test"><transmitter addr="{}"><resp status="comm test done"/>'.format(addr2_right),
#                      str(cls.msg))  # 断言通信是否成功
#         cls.assertIn('<ind type="comm test"><transmitter addr="{}"><resp status="comm test done"/>'.format(addr3_right),
#                      str(cls.msg))  # 断言通信是否成功
#         print("断言'启用通信测试命令'通过！")
#
#     # 启用通信测试命令:--基站全部离线状态
#     @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
#     def test08002_comm_test_error(cls):
#         addr1_right = "1aa6083cf920a18"  # 正确存在的基站
#         addr2_right = "1aa6083cf920914"  # 正确存在的基站
#         addr3_right = "1aa6083cf91cb9e"  # 正确存在的基站
#         print('启用通信测试命令--基站全部离线状态:[{},{},{}]'.format(addr1_right, addr2_right, addr3_right))
#         # 其中count是发送测试数据包的次数，1~65535；period是每次发送的间隔，单位毫秒ms，0~255
#         instruct = '<req type="comm test" count="100" period="10"><anchor ' \
#                    'addr = "{}" />' \
#                    '<anchor addr = "{}" /></req>'.format(addr1_right, addr2_right, addr3_right)  # 指令
#
#         # duration是次序发送连续帧的时长 单位秒
#         print("请求的数据：", instruct)
#         cls.msg = cls.oder.yq_response2(instruct)
#
#         a = 0
#         for i in cls.msg:
#             print("服务器返回的数据{}：".format(a), i)
#             a += 1
#
#         cls.assertNotIn('status="comm test done"', str(cls.msg))  # 断言响应里没有成功的状态
#         print("断言'启用通信测试命令'通过！")
#
#     # 启用通信测试命令: --基站3个在线状态只有一个离线状态
#     @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
#     def test08003_comm_test_error(cls):
#
#         addr_error = "1aa6083cf920914"
#         addr1 = "1aa6083cf91cb9d"
#         addr2 = "1aa6083cf920a17"
#         addr3 = "1aa6083cf920913"
#         print('启用通信测试命令:--基站三个在线状态[{},{},{}]一个离线状态[{}]'.format(addr1, addr2, addr3, addr_error))
#
#         instruct = '<req type="comm test" count="100" period="10">' \
#                    '<anchor addr = "{}" /><anchor addr = "{}" />' \
#                    '<anchor addr = "{}" /><anchor addr = "{}" /></req>'.format(addr1, addr2, addr3, addr_error)  # 指令
#
#         print("请求的数据：", instruct)
#         cls.msg = cls.oder.yq_response2(instruct)
#
#         a = 0
#         for i in cls.msg:
#             print("服务器返回的数据{}：".format(a), i)
#             a += 1
#         # 断言通信是否成功
#         cls.assertIn('<ind type="comm test"><transmitter addr="{}"><resp status="comm test done"/>'.format(addr1),
#                      str(cls.msg))  # 断言通信离线基站连接成功的状态
#         cls.assertIn('<ind type="comm test"><transmitter addr="{}"><resp status="comm test done"/>'.format(addr2),
#                      str(cls.msg))  # 断言通信离线基站连接成功的状态
#         cls.assertIn('<ind type="comm test"><transmitter addr="{}"><resp status="comm test done"/>'.format(addr3),
#                      str(cls.msg))  # 断言通信离线基站连接成功的状态
#         cls.assertIn('<ind type="comm test"><transmitter addr="{}"><resp status="not connected"/>'.format(addr_error),
#                      str(cls.msg))  # 断言通信离线基站连接未成功的状态
#         print("断言启用通信测试命令:--基站三个在线状态[{},{},{}]一个离线状态[{}]状态全部通过".format(addr1, addr2, addr3, addr_error))
#
#
# # 启用功率测试
# class Test_power_test(unittest.TestCase):
#     status = 99
#
#     @classmethod
#     def setUpClass(cls):
#         cls.oder = Test_api()
#         cls.status = unit.server_state
#         cls.msg = []
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.oder.close()
#
#     # 启用功率测试--基站全部正常在线
#     @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
#     def test09001_power_test(cls):
#         addr1 = '1aa6083cf920a17'  # 在线基站
#         addr2 = '1aa6083cf920913'  # 在线基站
#         addr3 = '1aa6083cf91cb9d'  # 在线基站
#         print('启用功率测试:--基站全部正常在线[{},{},{}]'.format(addr1, addr2, addr3))
#         instruct = '<req type="power test" duration="1">' \
#                    '<anchor addr = "{}" /><anchor addr = "{}" />' \
#                    '<anchor addr = "{}" /></req>'.format(addr1, addr2, addr3)  # 指令
#         # duration是次序发送连续帧的时长 单位秒
#         print("请求的数据：", instruct)
#         cls.msg = cls.oder.yq_response3(instruct)
#         a = 0
#         for i in cls.msg:
#             print("服务器返回的数据{}：".format(a), i)
#             a += 1
#         # 断言
#         cls.assertIn('<ind type="power test" addr="{}" status="power test done"/></ind>'.format(addr1),
#                      str(cls.msg))  # 断言
#         print("断言'启用功率测试--在线的基站{}测试'通过！".format(addr1))
#         cls.assertIn('<ind type="power test" addr="{}" status="power test done"/></ind>'.format(addr2),
#                      str(cls.msg))  # 断言
#         print("断言'启用功率测试--在线的基站{}测试'通过！".format(addr2))
#         cls.assertIn('<ind type="power test" addr="{}" status="power test done"/></ind>'.format(addr3),
#                      str(cls.msg))  # 断言
#         print("断言'启用功率测试--在线的基站{}测试'通过！".format(addr3))
#
#     # 启用功率测试--基站adrr有一个基站在线，其他基站离线和字符长度错误基站时
#     @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
#     def test09002_power_test_error1(cls):
#         addr = '1aa6083cf920a17'  # 在线基站
#
#         addr_error1 = '1aa6083cf920a18'  # 离线基站
#         addr_error2 = '1aa6083c'  # 8位的16进制字符基站
#         addr_error3 = '1afa6083cf91cb9ebcdefab'  # 17位16进制的字符基站
#         addr_error4 = '1aax6083c'  # 超出16进制字符标准的基站
#         print('启用功率测试-0-基站adrr[{}]有一个在线，2个基站[{},{}]出现字符长度错误、一个含有超出字母a到F的字符的基站addr：[{}]、一个[{}]离线时:'.format(addr,
#                                                                                                           addr_error2,
#                                                                                                           addr_error3,
#                                                                                                           addr_error1,
#                                                                                                           addr_error4))
#         instruct = '<req type="power test" duration="1">' \
#                    '<anchor addr="{}" />' \
#                    '<anchor addr = "{}" />' \
#                    '<anchor addr = "{}" />' \
#                    '<anchor addr = "{}" />' \
#                    '<anchor addr = "{}" /></req>'.format(addr, addr_error1, addr_error2, addr_error3, addr_error4)  # 指令
#         print("请求的数据：", instruct)
#         cls.msg = cls.oder.yq_response3(instruct)
#         a = 0
#         for i in cls.msg:
#             print("服务器返回的数据{}：".format(a), i)
#             a += 1
#         cls.assertIn('<ind type="power test" addr="{}" status="power test done"/></ind>'.format(addr),
#                      str(cls.msg))  # 断言
#         print("断言'启用功率测试--在线的基站{}测试'通过！".format(addr))
#         cls.assertIn('<ind type="power test" addr="{}" status="not connected"/></ind>'.format(addr_error1),
#                      str(cls.msg))  # 断言
#         print("断言'启用功率测试--离线的基站{}测试'通过！".format(addr_error1))
#         cls.assertIn('<ind type="power test" addr="{}" status="not connected"/></ind>'.format(addr_error2),
#                      str(cls.msg))  # 断言
#         print("断言'启用功率测试--离线的基站{}测试'通过！".format(addr_error2))
#         cls.assertIn('<ind type="power test" addr="{}" status="not connected"/></ind>'.format(addr_error3),
#                      str(cls.msg))  # 断言
#         print("断言'启用功率测试--离线的基站{}测试'通过！".format(addr_error3))
#
#     # 启用功率测试--基站adrr全部出现错误或者离线时
#     @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
#     def test09003_power_test_error2(cls):
#         addr1 = "1aa6083cf920a19"
#         addr2 = "1aa6083cf920914"
#         addr3 = "1aa6083cf91cb9e"
#         print('启用功率测试--基站adrr全部出现错误或者离线时:')
#         instruct = '<req type="power test" duration="10">' \
#                    '<anchor addr = "{}" />' \
#                    '<anchor addr = "{}" />' \
#                    '<anchor addr = "{}" /></req>'.format(addr1, addr2, addr3)  # 指令
#
#         cls.msg = cls.oder.yq_response3_error(instruct)
#         a = 0
#         for i in cls.msg:
#             print("服务器返回的数据{}：".format(a), i)
#             a += 1
#
#         cls.assertIn('status="not connected"', str(cls.msg))  # 断言
#         print("断言'启用功率测试--基站adrr出现错误或者离线时'通过！")
#
#
# # 重启基站
# class Test_reset_appoint_anchor(unittest.TestCase):
#     status = 99
#
#     @classmethod
#     def setUpClass(cls):
#         cls.oder = Test_api()
#         cls.status = unit.server_state
#         cls.msg = []
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.oder.close()
#
#     # 指定基站重启
#     @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
#     def test10001_reset_appoint_anchor(cls):
#         addr = '1aa6083cf920913'
#         print('指定基站addr={}:重启'.format(addr))
#         instruct = '<req type="anchor reset"><anchor addr = "{}" /></req>'.format(addr)  # 指令
#         print("请求的数据：", instruct)
#         cls.msg = cls.oder.yq_response(instruct)
#         print("服务器返回的数据：", str(cls.msg, 'utf8'))
#         cls.assertIn('<ind type="anchor reset"/>', str(cls.msg, 'utf8'))  # 断言
#         print("断言'重启指定基站'通过！")
#
#     # 重启全部基站
#     @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
#     def test10002_reset_anchor(cls):
#         print('重启全部基站:')
#         instruct = '<req type="anchor reset"/>'  # 指令
#         print("请求的数据：", instruct)
#         cls.msg = cls.oder.yq_response(instruct)
#         print("服务器返回的数据：", str(cls.msg, 'utf8'))
#         print("断言'重启全部基站'通过！")
#
#
# # 诊断信息配置命令
# class Test_log_cfg(unittest.TestCase):
#     status = 99
#
#     @classmethod
#     def setUpClass(cls):
#         cls.oder = Test_api()
#         cls.status = unit.server_state
#         cls.msg = []
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.oder.close()
#
#     # 诊断信息配置命令--全部基站在线状态
#     @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
#     def test11001_log_cfg(cls):
#         # 全部基站在线状态
#         addr1 = "1aa6083cf91cb9d"  # 主时间同步基站
#         addr2 = "1aa6083cf920a17"
#         addr3 = "1aa6083cf920913"
#         print('诊断信息配置命令--全部基站在线状态:[{},{},{}]'.format(addr1, addr2, addr3))
#         instruct = '<req type="log cfg"><anchor addr="{}" ' \
#                    'rxdiag_on="1" accum_on="1" accum_type="1"/>' \
#                    '<anchor addr="{}" rxdiag_on="0" accum_on="0" accum_type="0"/>' \
#                    '<anchor addr="{}" rxdiag_on="0" accum_on="0" accum_type="0"/>' \
#                    '</req>'.format(addr1, addr2, addr3)  # 指令
#         print("请求的数据：", instruct)
#         cls.msg = cls.oder.yq_response(instruct)
#         print("服务器返回的数据：", str(cls.msg, 'utf8'))
#         '''断言'''
#         cls.assertIn('<anchor addr="{}" status="config sent"/>'.format(addr1), str(cls.msg, 'utf8'))  # 断言
#         print("断言'诊断[{}]信息配置命令'通过！".format(addr1))
#         cls.assertIn('<anchor addr="{}" status="config sent"/>'.format(addr2), str(cls.msg, 'utf8'))  # 断言
#         print("断言'诊断[{}]信息配置命令'通过！".format(addr2))
#         cls.assertIn('<anchor addr="{}" status="config sent"/>'.format(addr3), str(cls.msg, 'utf8'))  # 断言
#         print("断言'诊断[{}]信息配置命令'通过！".format(addr3))
#
#     # 诊断信息配置命令--有一个基站离线状态其他在线
#     @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
#     def test11002_log_cfg(cls):
#         addr1 = "1aa6083cf91cb9d"  # 基站在线状态
#         addr2 = "1aa6083cf920a17"  # 基站在线状态
#         addr3 = "1aa6083cf920913"  # 基站离线状态
#         addr_error = "1aa6083cf920914"  # 基站离线状态
#         print('诊断信息配置命令--有一个基站离线状态其他在线:在线基站[{},{},{}],离线基站[{}]'.format(addr1, addr2, addr3, addr_error))
#         instruct = '<req type="log cfg"><anchor addr="{}" ' \
#                    'rxdiag_on="1" accum_on="1" accum_type="1"/>' \
#                    '<anchor addr="{}" rxdiag_on="0" accum_on="0" accum_type="0"/>' \
#                    '<anchor addr="{}" rxdiag_on="0" accum_on="0" accum_type="0"/>' \
#                    '<anchor addr="{}" rxdiag_on="0" accum_on="0" accum_type="0"/>' \
#                    '</req>'.format(addr1, addr2, addr3, addr_error)  # 指令
#         print("请求的数据：", instruct)
#         cls.msg = cls.oder.yq_response(instruct)
#         print("服务器返回的数据：", str(cls.msg, 'utf8'))
#         '''断言'''
#         cls.assertIn('<anchor addr="{}" status="config sent"/>'.format(addr1), str(cls.msg, 'utf8'))  # 断言
#         print("断言'诊断在线基站[{}]信息配置命令'通过！".format(addr1))
#         cls.assertIn('<anchor addr="{}" status="config sent"/>'.format(addr2), str(cls.msg, 'utf8'))  # 断言
#         print("断言'诊断在线基站[{}]信息配置命令'通过！".format(addr2))
#         cls.assertIn('<anchor addr="{}" status="config sent"/>'.format(addr3), str(cls.msg, 'utf8'))  # 断言
#         print("断言'诊断在线基站[{}]信息配置命令'通过！".format(addr3))
#         cls.assertIn('<anchor addr="{}" status="not connected"/>'.format(addr_error), str(cls.msg, 'utf8'))  # 断言
#         print("断言'诊断离线基站[{}]信息配置命令'通过！".format(addr3))
