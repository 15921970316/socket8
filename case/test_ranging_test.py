# 双向测距测试用例
from api.anchor_cfg import anchor_cfgs, anchor_list, ranging_test
from api.jzyq_api import Test_api
import unittest
import time
import unit

filename = unit.BASE_DIR + "\data\engine_Data.json"


# 双向测距
class Test_ranging_test(unittest.TestCase):
    status = 99
    from api.anchor_cfg import ranging_test
    @classmethod
    def setUpClass(cls):
        cls.oder = Test_api()
        cls.status = unit.server_state
        cls.ranging_test = ranging_test()
        cls.msg = []

    @classmethod
    def tearDownClass(cls):
        cls.oder.close()

    ## 4个基站之间的双向测距 -num_ranges=100 reverse=1
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test_ranging_test1(cls):
        print("双向测距！")
        filename = unit.BASE_DIR + "\data\engine_Data.json"
        json1 = unit.read_name_data(filename, "ranging_test_data1")

        cls.msg = cls.ranging_test.ranging_test(json1[0][0], json1[0][1], json1[0][2], json1[0][3], addr1=json1[0][4],
                                                addr2=json1[0][5], addr3=json1[0][6], addr4=json1[0][7])
        a = 0
        for i in cls.msg:
            print("服务器返回的数据{}：".format(a), i)
            a += 1
        # 断言响应
        cls.assertIn('<ind type="system status" msg="range measurement completes"></ind>', str(cls.msg))
        print("断言'双向测距'通过！")

    ## 3个基站之间的双向测距 -num_ranges=100 reverse=1
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test_ranging_test2(cls):
        print("双向测距！")
        filename = unit.BASE_DIR + "\data\engine_Data.json"
        json1 = unit.read_name_data(filename, "ranging_test_data1")

        cls.msg = cls.ranging_test.ranging_test(json1[0][0], json1[0][1], json1[0][2], json1[0][3], addr1=json1[0][4],
                                                addr2=json1[0][5],  addr4=json1[0][7])
        a = 0
        for i in cls.msg:
            print("服务器返回的数据{}：".format(a), i)
            a += 1
        # 断言响应
        cls.assertIn('<ind type="system status" msg="range measurement completes"></ind>', str(cls.msg))
        print("断言'双向测距'通过！")

    ## 3个基站之间的双向测距-num_ranges=-1 reverse=1
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test_ranging_test3(cls):
        print("双向测距！--每两个基站间的该轮测距执行TWR的次数num_ranges=-1")
        filename = unit.BASE_DIR + "\data\engine_Data.json"
        json1 = unit.read_name_data(filename, "ranging_test_data2")

        cls.msg = cls.ranging_test.ranging_test(json1[0][0], json1[0][1], json1[0][2], json1[0][3], addr1=json1[0][4],
                                                addr2=json1[0][5],  addr4=json1[0][7])
        a = 0
        for i in cls.msg:
            print("服务器返回的数据{}：".format(a), i)
            a += 1
        # 断言响应
        cls.assertIn('<ind type="system status" msg="range measurement completes"></ind>', str(cls.msg))
        print("断言'双向测距'通过！")

    ## 4个基站之间的双向测距-reverse="0" num_ranges=100
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test_ranging_test4(cls):
        print("双向测距！--reverse=0 表示每个指定基站会作为发起者与其后面的指定基站进行双向测距")
        filename = unit.BASE_DIR + "\data\engine_Data.json"
        json1 = unit.read_name_data(filename, "ranging_test_data3")

        cls.msg = cls.ranging_test.ranging_test(json1[0][0], json1[0][1], json1[0][2], json1[0][3], addr1=json1[0][4],
                                                addr2=json1[0][5], addr3=json1[0][6], addr4=json1[0][7])
        a = 0
        for i in cls.msg:
            print("服务器返回的数据{}：".format(a), i)
            a += 1
        # 断言响应
        cls.assertIn('<ind type="system status" msg="range measurement completes"></ind>', str(cls.msg))
        print("断言'双向测距'通过！")

    ## 4个基站之间的双向测距-reverse=1  num_ranges=100
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test_ranging_test5(cls):
        print("双向测距！--reverse=0 表示每个指定基站会作为发起者与其后面的指定基站进行双向测距")
        filename = unit.BASE_DIR + "\data\engine_Data.json"
        json1 = unit.read_name_data(filename, "ranging_test_data4")

        cls.msg = cls.ranging_test.ranging_test(json1[0][0], json1[0][1], json1[0][2], json1[0][3], addr1=json1[0][4],
                                                addr2=json1[0][5], addr3=json1[0][6], addr4=json1[0][7])
        a = 0
        for i in cls.msg:
            print("服务器返回的数据{}：".format(a), i)
            a += 1
        # 断言响应
        cls.assertIn('<ind type="system status" msg="range measurement completes"></ind>', str(cls.msg))
        print("断言'双向测距'通过！")
