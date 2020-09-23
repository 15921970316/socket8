#  设置定位算法参数测试用例
from api.anchor_cfg import anchor_cfgs
from api.jzyq_api import Test_api
import unittest
import time
import unit

filename = unit.BASE_DIR + "\data\engine_Data.json"
# 设置定位算法参数
class Test_multilateration(unittest.TestCase):
    status = 99

    @classmethod
    def setUpClass(cls):
        cls.oder = Test_api()
        cls.status = unit.server_state
        cls.msg = []

    @classmethod
    def tearDownClass(cls):
        cls.oder.close()

    # 定位算法配置命令
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test03001_anchor_multilateration(cls):
        print('定位算法配置命令:')
        # 指令
        instruct = '<req type="multilateration" algorithm="3"/>'
        print("请求的数据：", instruct)
        cls.msg = cls.oder.yq_response(instruct)
        print("服务器返回的数据：", str(cls.msg, 'utf8'))
        # 断言响应
        cls.assertIn('<ind type="multilateration"/>', str(cls.msg, 'utf8'))
        print("断言'定位算法配置命令'通过！")
