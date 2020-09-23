# 诊断信息配置测试用例
from api.anchor_cfg import anchor_cfgs
from api.jzyq_api import Test_api
import unittest
import time
import unit

filename = unit.BASE_DIR + "\data\engine_Data.json"
# 诊断信息配置命令
class Test_log_cfg(unittest.TestCase):
    status = 99

    @classmethod
    def setUpClass(cls):
        cls.oder = Test_api()
        cls.status = unit.server_state
        cls.msg = []

    @classmethod
    def tearDownClass(cls):
        cls.oder.close()

    # 诊断信息配置命令--全部基站在线状态
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test11001_log_cfg(cls):
        # 全部基站在线状态
        addr1 = "1aa6083cf91cb9d"  # 主时间同步基站
        addr2 = "1aa6083cf920a17"
        addr3 = "1aa6083cf920913"
        print('诊断信息配置命令--全部基站在线状态:[{},{},{}]'.format(addr1, addr2, addr3))
        instruct = '<req type="log cfg"><anchor addr="{}" ' \
                   'rxdiag_on="1" accum_on="1" accum_type="1"/>' \
                   '<anchor addr="{}" rxdiag_on="0" accum_on="0" accum_type="0"/>' \
                   '<anchor addr="{}" rxdiag_on="0" accum_on="0" accum_type="0"/>' \
                   '</req>'.format(addr1, addr2, addr3)  # 指令
        print("请求的数据：", instruct)
        cls.msg = cls.oder.yq_response(instruct)
        print("服务器返回的数据：", str(cls.msg, 'utf8'))
        '''断言'''
        cls.assertIn('<anchor addr="{}" status="config sent"/>'.format(addr1), str(cls.msg, 'utf8'))  # 断言
        print("断言'诊断[{}]信息配置命令'通过！".format(addr1))
        cls.assertIn('<anchor addr="{}" status="config sent"/>'.format(addr2), str(cls.msg, 'utf8'))  # 断言
        print("断言'诊断[{}]信息配置命令'通过！".format(addr2))
        cls.assertIn('<anchor addr="{}" status="config sent"/>'.format(addr3), str(cls.msg, 'utf8'))  # 断言
        print("断言'诊断[{}]信息配置命令'通过！".format(addr3))

    # 诊断信息配置命令--有一个基站离线状态其他在线
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test11002_log_cfg(cls):
        addr1 = "1aa6083cf91cb9d"  # 基站在线状态
        addr2 = "1aa6083cf920a17"  # 基站在线状态
        addr3 = "1aa6083cf920913"  # 基站离线状态
        addr_error = "1aa6083cf920914"  # 基站离线状态
        print('诊断信息配置命令--有一个基站离线状态其他在线:在线基站[{},{},{}],离线基站[{}]'.format(addr1, addr2, addr3, addr_error))
        instruct = '<req type="log cfg"><anchor addr="{}" ' \
                   'rxdiag_on="1" accum_on="1" accum_type="1"/>' \
                   '<anchor addr="{}" rxdiag_on="0" accum_on="0" accum_type="0"/>' \
                   '<anchor addr="{}" rxdiag_on="0" accum_on="0" accum_type="0"/>' \
                   '<anchor addr="{}" rxdiag_on="0" accum_on="0" accum_type="0"/>' \
                   '</req>'.format(addr1, addr2, addr3, addr_error)  # 指令
        print("请求的数据：", instruct)
        cls.msg = cls.oder.yq_response(instruct)
        print("服务器返回的数据：", str(cls.msg, 'utf8'))
        '''断言'''
        cls.assertIn('<anchor addr="{}" status="config sent"/>'.format(addr1), str(cls.msg, 'utf8'))  # 断言
        print("断言'诊断在线基站[{}]信息配置命令'通过！".format(addr1))
        cls.assertIn('<anchor addr="{}" status="config sent"/>'.format(addr2), str(cls.msg, 'utf8'))  # 断言
        print("断言'诊断在线基站[{}]信息配置命令'通过！".format(addr2))
        cls.assertIn('<anchor addr="{}" status="config sent"/>'.format(addr3), str(cls.msg, 'utf8'))  # 断言
        print("断言'诊断在线基站[{}]信息配置命令'通过！".format(addr3))
        cls.assertIn('<anchor addr="{}" status="not connected"/>'.format(addr_error), str(cls.msg, 'utf8'))  # 断言
        print("断言'诊断离线基站[{}]信息配置命令'通过！".format(addr3))
