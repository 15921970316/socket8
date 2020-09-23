# 导包
import os
import unittest
import HTMLTestRunner_PY3
import time
# 创建测试套件
# from case.test_jzyq \
#     import Test_anchor_cfg, Test_anchor_list, Test_comm_test, Test_rtls_start_stop, Test_multilateration, \
#     Test_antenna_cfg, Test_log_cfg, Test_power_test, Test_ranging_test, Test_reset_appoint_anchor, Test_rf_cfg, Test_rtls_status
from case.test_anchor import Test_anchor_cfgs,Test_anchor_lists
from case.test_antenna_cfg import Test_antenna_cfg
from case.test_comm_test import Test_comm_test
from case.test_log_cfg import Test_log_cfg
from case.test_multilateration import Test_multilateration
from case.test_power_test import Test_power_test
from case.test_ranging_test import Test_ranging_test
from case.test_reset_appoint_anchor import Test_reset_appoint_anchor
from case.test_rf_cfg import Test_rf_cfg
from case.test_rtls_start_stop import Test_rtls_start_stop, Test_rtls_status

suite = unittest.TestSuite()
# # 将测试用例添加到测试套件
suite.addTest(unittest.makeSuite(Test_anchor_cfgs))  # 基站配置接口测试
suite.addTest(unittest.makeSuite(Test_anchor_lists))  # 查询基站列表接口测试
suite.addTest(unittest.makeSuite(Test_multilateration))  # 定位算法配置命令接口测试
suite.addTest(unittest.makeSuite(Test_rf_cfg))  # 射频配置命令接口测试
suite.addTest(unittest.makeSuite(Test_antenna_cfg))  # 定位天线延迟配置接口测试
suite.addTest(unittest.makeSuite(Test_comm_test))  # 通信测试命令接口测试
suite.addTest(unittest.makeSuite(Test_power_test))  # 功率测试接口测试
suite.addTest(unittest.makeSuite(Test_ranging_test))  # 双向测距接口测试
suite.addTest(unittest.makeSuite(Test_log_cfg))  # 诊断信息配置命令接口测试
suite.addTest(unittest.makeSuite(Test_rtls_start_stop))  # 启、停定位接口测试
suite.addTest(unittest.makeSuite(Test_rtls_status))  # 定位和定位状态接口测试
suite.addTest(unittest.makeSuite(Test_reset_appoint_anchor))  # 重启基站接口测试


# suite.addTest(Test_oder('test01002_anchor_cfg_Error'))#接口测试
# 定义测试报告的名称
t = time.time()
s = int(round(t * 1000))
report_name = os.path.dirname(os.path.abspath(__file__)) + "/report/test_info.html"
# 使用HTMLTestRunner_PY3生成测试报告
with open(report_name, 'wb') as f:
    # 实例化HTMLTestRunner_PY3
    runner = HTMLTestRunner_PY3.HTMLTestRunner(f, verbosity=1, title="引擎测试报告", description="引擎系统的测试报告")
    # 使用runner运行测试套件
    runner.run(suite)
