import os

server_state=-10
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# 通用断言函数
import json


def assert_common(httpcode, success, code, message, response, self):
    self.assertEqual(httpcode, response.status_code)  #
    self.assertEqual(success, response.json().get(""))  #
    self.assertEqual(code, response.json().get(""))  #
    self.assertIn(message, response.json().get(""))  #

#
# 1 定义读取数据的函数，并从外界接收文件名
def read_data(filename):

    # 2 使用内置函数open打开外界传入的文件名
    with open(filename, mode='r', encoding='utf-8') as f:

        # 3 使用内置模块json加载文件
        jsonData = json.load(f)
        # 定义一个存放数据的空列表
        result_list = list()
        # 拼接数据成一个嵌套元组的形式
        for data in jsonData:
            result_list.append(tuple(data.values()))
        #   return 返回
        f.close()
    return result_list
def get_json_data(json_path):
    # 获取json里面数据

    with open(json_path, 'rb') as f:
        # 定义为只读模型，并定义名称为f
        params = json.load(f)
        # 加载json文件中的内容给params
    f.close()
    # 关闭json读模式
    return params
# 1 定义读取模块数据的函数，并从外界接收数据文件路径和要读取的接口模块
def read_name_data(filename, name):
    # 2 使用内置函数open打开外界传入的文件名
    with open(filename, mode='r', encoding='utf-8') as f:
        # 3 使用内置模块json加载文件
        jsonData = json.load(f)
        # 4 读取数据
        data = jsonData.get(name)
        # 定义存放数据的空列表
        result_list = list()
        # 讲数据转化为元组后添加到列表中
        result_list.append(tuple(data.values()))
    # 5 打印结果，并return返回
        f.close()
    return result_list


