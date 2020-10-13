# 射频配置命令测试用例
from api.anchor_cfg import anchor_cfgs
from api.jzyq_api import Test_api
import unittest
import time
import unit

filename = unit.BASE_DIR + "\data\engine_Data.json"
# 射频配置命令
class Test_rf_cfg(unittest.TestCase):
    status = 99

    @classmethod
    def setUpClass(cls):
        cls.oder = Test_api()
        cls.status = unit.server_state
        cls.msg = []

    @classmethod
    def tearDownClass(cls):
        cls.oder.close()

    # 射频配置命令
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test07001_rf_cfg(cls):
        print('射频配置命令:')
        # 其中count是发送测试数据包的次数，1~65535；period是每次发送的间隔，单位毫秒ms，0~255
        instruct = '<req type="rf cfg"><rf chan="2" prf="64" rate="6810" code="9" plen="128" pac="8" nsfd="0"/></req>'  # 指令

        print("请求的数据：", instruct)
        cls.msg = cls.oder.yq_response(instruct)

        print("服务器返回的数据：", cls.msg)
        cls.assertIn('status="config sent"', str(cls.msg))  # 断言
        print("断言'射频配置命令'通过！")





