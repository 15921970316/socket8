# 基站重启测试用例
from api.anchor_cfg import anchor_cfgs
from api.jzyq_api import Test_api
import unittest
import time
import unit

filename = unit.BASE_DIR + "\data\engine_Data.json"
class Test_reset_appoint_anchor(unittest.TestCase):
    status = 99

    @classmethod
    def setUpClass(cls):
        cls.oder = Test_api()
        cls.status = unit.server_state
        cls.msg = []

    @classmethod
    def tearDownClass(cls):
        cls.oder.close()

    # 指定基站重启
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test10001_reset_appoint_anchor(cls):
        addr = '1aa6083cf920913'
        print('指定基站addr={}:重启'.format(addr))
        instruct = '<req type="anchor reset"><anchor addr = "{}" /></req>'.format(addr)  # 指令
        print("请求的数据：", instruct)
        cls.msg = cls.oder.yq_response(instruct)
        print("服务器返回的数据：", str(cls.msg, 'utf8'))
        cls.assertIn('<ind type="anchor reset"/>', str(cls.msg, 'utf8'))  # 断言
        print("断言'重启指定基站'通过！")

    # 重启全部基站
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test10002_reset_anchor(cls):
        print('重启全部基站:')
        instruct = '<req type="anchor reset"/>'  # 指令
        print("请求的数据：", instruct)
        cls.msg = cls.oder.yq_response(instruct)
        print("服务器返回的数据：", str(cls.msg, 'utf8'))
        print("断言'重启全部基站'通过！")
