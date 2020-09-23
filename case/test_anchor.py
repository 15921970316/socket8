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
    def test01001_anchor_cfg(cls):
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
    def test01002_anchor_cfg(cls):
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
    def test01003_anchor_cfg(cls):
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
    def test01004_anchor_cfg_addr(cls):
        print('基站进行配置--对addr为空的基站进行配置')
        filename = unit.BASE_DIR + "\data\engine_Data.json"
        json1 = unit.read_name_data(filename, "data5")
        cls.msg = cls.anchor_cfg1.anchor_cfg_one(json1)
        print("服务器返回的数据：", str(cls.msg, 'utf8'))
        cls.assertIn('<anchor addr="{}" db="config saved" status="not connected"/>'.format(json1[0][0]),
                     str(cls.msg, 'utf8'))
        print("断言'{}'配置通过！".format(json1[0][0]))

# 对addr为纯数字的基站进行配置
    @unittest.skipIf(status == -1, u"状态码等于-1，就跳过该测试")
    def test01005_anchor_cfg_addr(cls):
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
    def test01007_anchor_cfg_addr(cls):
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
    def test01008_anchor_cfg_addr(cls):
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
    def test01009_anchor_cfg_addr(cls):
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
    def test010010_anchor_cfg_addr(cls):
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
    def test010011_anchor_cfg_addr(cls):
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
    def test010011_anchor_cfg_syncref(cls):
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
    def test010012_anchor_cfg_syncref(cls):
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
    def test010013_anchor_cfg_syncref(cls):
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
    def test010014_anchor_cfg_syncref(cls):
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
    def test010015_anchor_cfg_syncref(cls):
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
    def test010016_anchor_cfg_syncref(cls):
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
    def test010017_anchor_cfg_syncref(cls):
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
    def test0100171_anchor_cfg_xyz(cls):
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
    def test0100172_anchor_cfg_xyz(cls):
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
    def test0100173_anchor_cfg_xyz(cls):
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
    def test0100174_anchor_cfg_xyz(cls):
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
    def test0100175_anchor_cfg_xyz(cls):
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
    def test_anchor_list(cls):
        print("基站列表查询")
        cls.msg = cls.anchor_list1.Test02001_anchor_list()
        print("服务器返回的数据：", cls.msg)
        cls.assertIn('<ind type="anchor list">',cls.msg)
        print("断言通过")
    def test_anchor_list_1000(cls):
        print("1000次循环")
        cls.msg = cls.anchor_list1.test02002_anchor_list()
        # print("服务器返回的数据：", cls.msg)
        cls.assertIn('<ind type="anchor list">', cls.msg)
        print("断言通过")
