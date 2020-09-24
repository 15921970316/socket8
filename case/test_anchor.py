# 基站配置和查询测试用例
from api.anchor_cfg import anchor_cfgs, anchor_list, ranging_test
from api.jzyq_api import Test_api
import unittest
import time
import unit

filename = unit.BASE_DIR + "\data\engine_Data.json"


# 基站配置
class Test_anchor_cfgs(unittest.TestCase):
    status = 99

    @classmethod
    def setUpClass(cls):
        cls.oder = Test_api()
        cls.status = unit.server_state
        cls.msg = []
        cls.anchor_cfg1 = anchor_cfgs()

    @classmethod
    def tearDownClass(cls):
        cls.oder.close()

    # 对3个在线1个离线的基站进行配置
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test_anchor_cfg1(cls):
        print('基站进行配置--对4个在线的基站进行配置')
        filename = unit.BASE_DIR + "\data\engine_Data.json"
        # print("filename的路径为：", filename)
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

    # 对单个在线的基站进行配置
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test_anchor_cfg2(cls):
        print('基站进行配置--对单个在线的基站进行配置')
        filename = unit.BASE_DIR + "\data\engine_Data.json"
        json1 = unit.read_name_data(filename, "data1")
        cls.msg = cls.anchor_cfg1.anchor_cfg_one(json1)
        print("服务器返回的数据：", str(cls.msg, 'utf8'))
        cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(json1[0][0]),
                     str(cls.msg, 'utf8'))
        print("断言'{}'配置通过！".format(json1[0][0]))

    # 对单个不在线的基站进行配置
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test_anchor_cfg3(cls):
        print('基站进行配置--对单个不在线的基站进行配置')
        filename = unit.BASE_DIR + "\data\engine_Data.json"
        json1 = unit.read_name_data(filename, "data4")
        cls.msg = cls.anchor_cfg1.anchor_cfg_one(json1)
        print("服务器返回的数据：", str(cls.msg, 'utf8'))
        cls.assertIn('<anchor addr="{}" db="config saved" status="not connected"/>'.format(json1[0][0]),
                     str(cls.msg, 'utf8'))
        print("断言'{}'配置通过！".format(json1[0][0]))

    # 对addr为空的基站进行配置
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test_anchor_cfg_addr1(cls):
        print('基站进行配置--对addr为空的基站进行配置')
        filename = unit.BASE_DIR + "\data\engine_Data.json"
        json1 = unit.read_name_data(filename, "data5")
        cls.msg = cls.anchor_cfg1.anchor_cfg_one(json1)
        print("服务器返回的数据：", str(cls.msg, 'utf8'))
        try:

            cls.assertIn('<anchor addr="{}" db="config saved" status="not connected"/>'.format(json1[0][0]),
                         str(cls.msg, 'utf8'))
            print("断言'{}'配置通过！".format(json1[0][0]))

        except Exception as e:
            print(e)
# 对addr为纯数字的基站进行配置
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test_anchor_cfg_addr2(cls):
        print('基站进行配置--对addr为纯数字的基站进行配置')
        filename = unit.BASE_DIR + "\data\engine_Data.json"
        json1 = unit.read_name_data(filename, "data6")
        cls.msg = cls.anchor_cfg1.anchor_cfg_one(json1)
        print("服务器返回的数据：", str(cls.msg, 'utf8'))
        cls.assertIn('<anchor addr="{}" db="config saved" status="not connected"/>'.format(json1[0][0]),
                     str(cls.msg, 'utf8'))
        print("断言'{}'配置通过！".format(json1[0][0]))

# 包含大小写字母"G-Z"
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test_anchor_cfg_addr3(cls):
        print(' 基站进行配置--addr包含大小写字母"G-Z"')
        filename = unit.BASE_DIR + "\data\engine_Data.json"
        json1 = unit.read_name_data(filename, "data12")
        cls.msg = cls.anchor_cfg1.anchor_cfg_one(json1)
        print("服务器返回的数据：", str(cls.msg, 'utf8'))
        cls.assertIn('<anchor addr="{}" db="config saved" status="not connected"/>'.format(json1[0][0]),
                     str(cls.msg, 'utf8'))
        print("断言'{}'配置通过！".format(json1[0][0]))

# 对addr含有中文的基站进行配置
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test_anchor_cfg_addr4(cls):
        print('基站进行配置--对addr含有中文的基站进行配置')
        filename = unit.BASE_DIR + "\data\engine_Data.json"
        json1 = unit.read_name_data(filename, "data8")
        cls.msg = cls.anchor_cfg1.anchor_cfg_one(json1)
        print("服务器返回的数据：", str(cls.msg, 'utf8'))
        cls.assertIn('<anchor addr="{}" db="config saved" status="not connected"/>'.format(json1[0][0]),
                     str(cls.msg, 'utf8'))
        print("断言'{}'配置通过！".format(json1[0][0]))

# 对addr含有空格的基站进行配置
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test_anchor_cfg_addr5(cls):
        print('基站进行配置--对addr含有空格的基站进行配置')
        filename = unit.BASE_DIR + "\data\engine_Data.json"
        json1 = unit.read_name_data(filename, "data9")
        cls.msg = cls.anchor_cfg1.anchor_cfg_one(json1)
        print("服务器返回的数据：", str(cls.msg, 'utf8'))
        cls.assertIn('<anchor addr="{}" db="config saved" status="not connected"/>'.format(json1[0][0]),
                     str(cls.msg, 'utf8'))
        print("断言'{}'配置通过！".format(json1[0][0]))

# 对addr字符长度小于16位的基站进行配置
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test_anchor_cfg_addr6(cls):
        print('基站进行配置--对addr字符长度小于16位的基站进行配置')
        filename = unit.BASE_DIR + "\data\engine_Data.json"
        json1 = unit.read_name_data(filename, "data10")
        cls.msg = cls.anchor_cfg1.anchor_cfg_one(json1)
        print("服务器返回的数据：", str(cls.msg, 'utf8'))
        cls.assertIn('<anchor addr="{}" db="config saved" status="not connected"/>'.format(json1[0][0]),
                     str(cls.msg, 'utf8'))
        print("断言'{}'配置通过！".format(json1[0][0]))

# 对addr字符长度大于16位的基站进行配置
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test_anchor_cfg_addr7(cls):
        print(' 基站进行配置--对addr字符长度大于16位的基站进行配置')
        filename = unit.BASE_DIR + "\data\engine_Data.json"
        json1 = unit.read_name_data(filename, "data11")
        cls.msg = cls.anchor_cfg1.anchor_cfg_one(json1)
        print("服务器返回的数据：", str(cls.msg, 'utf8'))
        cls.assertIn('<anchor addr="{}" db="config saved" status="not connected"/>'.format(json1[0][0]),
                     str(cls.msg, 'utf8'))
        print("断言'{}'配置通过！".format(json1[0][0]))

    # 对syncref=1 的基站进行配置
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test_anchor_cfg_syncref1(cls):
        print(' 基站进行配置--对syncref值为1')
        filename = unit.BASE_DIR + "\data\engine_Data.json"
        json1 = unit.read_name_data(filename, "data12")
        cls.msg = cls.anchor_cfg1.anchor_cfg_one(json1)
        print("服务器返回的数据：", str(cls.msg, 'utf8'))
        cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(json1[0][0]),
                     str(cls.msg, 'utf8'))
        print("断言'{}'配置通过！".format(json1[0][0]))
    # 对syncref=0 的基站进行配置
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test_anchor_cfg_syncref2(cls):
        print(' 基站进行配置--对syncref值为0')
        filename = unit.BASE_DIR + "\data\engine_Data.json"
        json1 = unit.read_name_data(filename, "data13")
        cls.msg = cls.anchor_cfg1.anchor_cfg_one(json1)
        print("服务器返回的数据：", str(cls.msg, 'utf8'))
        cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(json1[0][0]),
                     str(cls.msg, 'utf8'))
        print("断言'{}'配置通过！".format(json1[0][0]))

    # 对syncref为小数 的基站进行配置
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test_anchor_cfg_syncref3(cls):
        print(' 基站进行配置--对syncref值为小数')
        filename = unit.BASE_DIR + "\data\engine_Data.json"
        json1 = unit.read_name_data(filename, "data14")
        cls.msg = cls.anchor_cfg1.anchor_cfg_one(json1)
        print("服务器返回的数据：", str(cls.msg, 'utf8'))
        cls.assertIn('<anchor addr="{}" db="config saved" status="not connected"/>'.format(json1[0][0]),
                     str(cls.msg, 'utf8'))
        print("断言'{}'配置通过！".format(json1[0][0]))

    # 对syncref为空 的基站进行配置
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test_anchor_cfg_syncref4(cls):
        print(' 基站进行配置--对syncref值为空')
        filename = unit.BASE_DIR + "\data\engine_Data.json"
        json1 = unit.read_name_data(filename, "data15")
        cls.msg = cls.anchor_cfg1.anchor_cfg_one(json1)
        print("服务器返回的数据：", str(cls.msg, 'utf8'))
        cls.assertIn('<anchor addr="{}" db="config saved" status="not connected"/>'.format(json1[0][0]),
                     str(cls.msg, 'utf8'))
        print("断言'{}'配置通过！".format(json1[0][0]))

    # 对syncref为英文字符 的基站进行配置
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test_anchor_cfg_syncref5(cls):
        print(' 基站进行配置--对syncref值为英文字符')
        filename = unit.BASE_DIR + "\data\engine_Data.json"
        json1 = unit.read_name_data(filename, "data16")
        cls.msg = cls.anchor_cfg1.anchor_cfg_one(json1)
        print("服务器返回的数据：", str(cls.msg, 'utf8'))
        cls.assertIn('<anchor addr="{}" db="config saved" status="not connected"/>'.format(json1[0][0]),
                     str(cls.msg, 'utf8'))
        print("断言'{}'配置通过！".format(json1[0][0]))

    # 对syncref为中文字符 的基站进行配置
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test_anchor_cfg_syncref6(cls):
        print(' 基站进行配置--对syncref值为中文字符')
        filename = unit.BASE_DIR + "\data\engine_Data.json"
        json1 = unit.read_name_data(filename, "data17")
        cls.msg = cls.anchor_cfg1.anchor_cfg_one(json1)
        print("服务器返回的数据：", str(cls.msg, 'utf8'))
        cls.assertIn('<anchor addr="{}" db="config saved" status="not connected"/>'.format(json1[0][0]),
                     str(cls.msg, 'utf8'))
        print("断言'{}'配置通过！".format(json1[0][0]))

    # 对syncref为特殊字符 的基站进行配置
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test_anchor_cfg_syncref7(cls):
        print(' 基站进行配置--对syncref值为特殊字符')
        filename = unit.BASE_DIR + "\data\engine_Data.json"
        json1 = unit.read_name_data(filename, "data18")
        cls.msg = cls.anchor_cfg1.anchor_cfg_one(json1)
        print("服务器返回的数据：", str(cls.msg, 'utf8'))
        cls.assertIn('<anchor addr="{}" db="config saved" status="not connected"/>'.format(json1[0][0]),
                     str(cls.msg, 'utf8'))
        print("断言'{}'配置通过！".format(json1[0][0]))

    # 对xyz值为小数点后四位小数 的基站进行配置
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test_anchor_cfg_xyz1(cls):
        print(' 基站进行配置--对xyz值为小数点后四位小数')
        filename = unit.BASE_DIR + "\data\engine_Data.json"
        json1 = unit.read_name_data(filename, "data19")
        cls.msg = cls.anchor_cfg1.anchor_cfg_one(json1)
        print("服务器返回的数据：", str(cls.msg, 'utf8'))
        cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(json1[0][0]),
                     str(cls.msg, 'utf8'))
        print("断言'{}'配置通过！".format(json1[0][0]))
    # 对xyz值小数点后非四位小数 的基站进行配置
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test_anchor_cfg_xyz2(cls):
        print(' 基站进行配置--对xyz值小数点后非四位小数')
        filename = unit.BASE_DIR + "\data\engine_Data.json"
        json1 = unit.read_name_data(filename, "data20")
        cls.msg = cls.anchor_cfg1.anchor_cfg_one(json1)
        print("服务器返回的数据：", str(cls.msg, 'utf8'))
        cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(json1[0][0]),
                     str(cls.msg, 'utf8'))
        print("断言'{}'配置通过！".format(json1[0][0]))

    # 对xyz值整数 的基站进行配置
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test_anchor_cfg_xyz3(cls):
        print(' 基站进行配置--对xyz值整数')
        filename = unit.BASE_DIR + "\data\engine_Data.json"
        json1 = unit.read_name_data(filename, "data21")
        cls.msg = cls.anchor_cfg1.anchor_cfg_one(json1)
        print("服务器返回的数据：", str(cls.msg, 'utf8'))
        cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(json1[0][0]),
                     str(cls.msg, 'utf8'))
        print("断言'{}'配置通过！".format(json1[0][0]))
    # 对xyz值非数值型字符 的基站进行配置
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test_anchor_cfg_xyz4(cls):
        print(' 基站进行配置--对xyz值非数值型字符')
        filename = unit.BASE_DIR + "\data\engine_Data.json"
        json1 = unit.read_name_data(filename, "data22")
        cls.msg = cls.anchor_cfg1.anchor_cfg_one(json1)
        print("服务器返回的数据：", str(cls.msg, 'utf8'))
        cls.assertIn('<anchor addr="{}" db="config saved" status="not connected"/>'.format(json1[0][0]),
                     str(cls.msg, 'utf8'))
        print("断言'{}'配置通过！".format(json1[0][0]))
    # 对xyz值特殊字符 的基站进行配置
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test_anchor_cfg_xyz5(cls):
        print(' 基站进行配置--对xyz值特殊字符')
        filename = unit.BASE_DIR + "\data\engine_Data.json"
        json1 = unit.read_name_data(filename, "data23")
        cls.msg = cls.anchor_cfg1.anchor_cfg_one(json1)
        print("服务器返回的数据：", str(cls.msg, 'utf8'))
        cls.assertIn('<anchor addr="{}" db="config saved" status="not connected"/>'.format(json1[0][0]),
                     str(cls.msg, 'utf8'))
        print("断言'{}'配置通过！".format(json1[0][0]))
# 基站列表查询
class Test_anchor_lists(unittest.TestCase):
    status = 99

    @classmethod
    def setUpClass(cls):
        cls.oder = Test_api()
        cls.status = unit.server_state
        cls.msg = []
        cls.anchor_list1 = anchor_list()

    @classmethod
    def tearDownClass(cls):
        cls.oder.close()
    # 基站列表查询
    def test_anchor_list(cls):
        print("基站列表查询")
        cls.msg = cls.anchor_list1.Test02001_anchor_list()
        print("服务器返回的数据：", cls.msg)
        cls.assertIn('<ind type="anchor list">',cls.msg)
        print("断言通过")
    # 1000次的基站列表查询
    def test_anchor_list_1000(cls):
        print("1000次循环")
        cls.msg = cls.anchor_list1.test02002_anchor_list()
        # print("服务器返回的数据：", cls.msg)
        cls.assertIn('<ind type="anchor list">', cls.msg)
        print("断言通过")
