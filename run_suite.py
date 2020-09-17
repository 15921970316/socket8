# 导包
import os
import unittest

import HTMLTestRunner_PY3

import time

# 创建测试套件
from case.test_jzyq import Test_oder

suite = unittest.TestSuite()
# 将测试用例添加到测试套件
suite.addTest(unittest.makeSuite(Test_oder))#接口测试套件

# 定义测试报告的名称
t=time.time()
s=int(round(t*1000))
report_name =  os.path.dirname(os.path.abspath(__file__)) + "/report/test_info.html"
# 使用HTMLTestRunner_PY3生成测试报告
with open(report_name, 'wb') as f:
    # 实例化HTMLTestRunner_PY3
    runner = HTMLTestRunner_PY3.HTMLTestRunner(f,verbosity=1,title="引擎测试报告", description="引擎系统的测试报告")
    # 使用runner运行测试套件
    runner.run(suite)



