# 启、停定位测试用例
from api.anchor_cfg import anchor_cfgs
from api.jzyq_api import Test_api
import unittest
import time
import unit

filename = unit.BASE_DIR + "\data\engine_Data.json"

# 启、停定位
class Test_rtls_start_stop(unittest.TestCase):
    status = 99

    @classmethod
    def setUpClass(cls):
        cls.oder = Test_api()
        cls.status = unit.server_state
        cls.msg = []

    @classmethod
    def tearDownClass(cls):
        cls.oder.close()

    # 开始定位
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test05001_start_positioning(cls):
        print('开始定位:')
        instruct = '<req type="rtls start"></req>'  # 指令
        print("请求的数据：", instruct)
        cls.msg = cls.oder.yq_response(instruct)

        print("服务器返回的数据：", str(cls.msg, 'utf8'))
        time.sleep(10)
        cls.assertIn('<ind type="rtls start"/>', str(cls.msg, 'utf8'))  # 断言
        print("断言'开始定位'通过！")

    # 停止定位
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test05003_Stop_positioning(cls):
        try:
            print('停止定位:')
            instruct = '<req type="rtls stop"/>'  # 指令
            print("请求的数据：", instruct)
            cls.msg = cls.oder.yq_response(instruct)

            print("服务器返回的数据：", str(cls.msg, 'utf8'))

            cls.assertIn('<ind type="rtls stop"/>', str(cls.msg, 'utf8'))  # 断言
            print("断言'停止定位'通过！")
        except Exception as e:
            print(e)

        # 停止定位后查询定位状态


# 定位状态
class Test_rtls_status(unittest.TestCase):
    status = 99

    @classmethod
    def setUpClass(cls):
        cls.oder = Test_api()
        cls.status = unit.server_state
        cls.msg = []

    @classmethod
    def tearDownClass(cls):
        cls.oder.close()

    # 开始定位后查询定位状态
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test05002_rtls_start_status(cls):
        print('开始定位:')
        instruct = '<req type="rtls start"></req>'  # 指令
        print("请求的数据：", instruct)
        cls.msg = cls.oder.yq_response(instruct)

        print("服务器返回的数据：", str(cls.msg, 'utf8'))
        time.sleep(10)
        cls.assertIn('<ind type="rtls start"/>', str(cls.msg, 'utf8'))  # 断言
        print("断言'开始定位'通过！")
        print('开始定位后查询定位状态:')
        instruct = '<req type="rtls state"/>'  # 指令
        print("请求的数据：", instruct)
        cls.msg = cls.oder.yq_response(instruct)

        print("服务器返回的数据：", str(cls.msg, 'utf8'))
        time.sleep(10)
        cls.assertIn('<ind type="rtls state" state="running"/>', str(cls.msg, 'utf8'))  # 断言
        print("断言'开始定位后查询定位状态'通过！")

    # 停止定位后查询定位状态
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test05004_rtls_stop_start(cls):
        try:
            print('停止定位:')
            instruct = '<req type="rtls stop"/>'  # 指令
            print("请求的数据：", instruct)
            cls.msg = cls.oder.yq_response(instruct)

            print("服务器返回的数据：", str(cls.msg, 'utf8'))

            cls.assertIn('<ind type="rtls stop"/>', str(cls.msg, 'utf8'))  # 断言
            print("断言'停止定位'通过！")
        except Exception as e:
            print(e)
        print('停止定位后查询定位状态:')
        instruct = '<req type="rtls state"/>'  # 指令
        print("请求的数据：", instruct)
        cls.msg = cls.oder.yq_response(instruct)

        print("服务器返回的数据：", str(cls.msg, 'utf8'))

        cls.assertIn('<ind type="rtls state" state="stopped"/>', str(cls.msg, 'utf8'))  # 断言
        print("断言'停止定位后查询定位状态'通过！")

