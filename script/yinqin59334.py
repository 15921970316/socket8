# 测试用例
from api.jzyq_api import Test_api
import time
import unit


class Oder_script():
    status=99

    @classmethod
    def setUpClass(cls):
        cls.oder = Test_api()
        cls.status= unit.server_state
        cls.msg = []

    @classmethod
    def tearDownClass(cls):
        cls.oder.close()


#对不在线基站进行配置

    def anchor_cfg_Error(cls,addr1_right,addr2_Error,addr3_Error,addr4_Error):
        # addr1_right   # 正确存在的基站
        # addr2_Error   # 错误或者不存在的基站
        # addr3_Error  # 错误或者不存在的基站
        # addr4_Error  # 错误或者不存在的基站
        print('对不在线的基站{},{},{}和在线的基站{}的同时进行配置命令!'.format( addr2_Error, addr3_Error, addr4_Error,addr1_right))
        # 指令
        instruct = '<req type="anchor cfg"><anchor addr="{}"' \
                   ' x="1.30" y="2.27" z="2.52" syncref="1" follow_addr="0" lag_delay="0"></anchor>' \
                   '<anchor addr="{}" x="7.93" y="0.87" z="2.53" syncref="0" ' \
                   'follow_addr="0" lag_delay="0"><syncrefanchor addr="1aa6083cf92080b"' \
                   ' rfdistance="0"/></anchor><anchor addr="{}" x="8.04" y="10.43" z="2.56" ' \
                   '' \
                   'syncref="0" follow_addr="0" lag_delay="0"><syncrefanchor addr="1aa6083cf92080b" ' \
                   'rfdistance="0"/></anchor><anchor addr="{}" x="1.44" y="9.66" z="2.53" ' \
                   'syncref="0" follow_addr="0" lag_delay="0"><syncrefanchor addr="1aa6083cf92080b" ' \
                   'rfdistance="0"/></anchor></req>'' '.format(addr1_right, addr2_Error, addr3_Error, addr4_Error)
        print("请求的数据：", instruct)

        cls.msg = cls.oder.yq_response(instruct)
        # 断言配置设置成功标识符status="config sent"已配置
        # cls.assertNotIn('status="config sent"', str(cls.msg, 'utf8'))
        print("服务器返回的数据：", str(cls.msg, 'utf8'))
        return cls.msg

# 对在线的基站进行配置

    def test001_anchor_cfg(cls):
            print('对在线的基站进行配置命令:')
            print(cls.status)
            addr1_right = "1aa6083cf920a17"  # 正确存在的基站
            addr2_right = "1aa6083cf920913"  # 正确存在的基站
            addr3_right = "1aa6083cf91cb9d"  # 正确存在的基站
            # addr4_right = "1aa6083cf920a17"  # 正确存在的基站
            # 指令
            instruct = '<req type="anchor cfg"><anchor addr="{}" x="1.30" y="2.27" z="2.52" syncref="1" ' \
                       'follow_addr="0" lag_delay="0"></anchor>' \
                       '<anchor addr="{}" x="7.93" y="0.87" z="2.53" syncref="0" follow_addr="0" lag_delay="0">' \
                       '<syncrefanchor addr="{}" rfdistance="0"/></anchor>' \
                       '<anchor addr="{}" x="8.04" y="10.43" z="2.56" ' \
                       'syncref="0" follow_addr="0" lag_delay="0"><syncrefanchor addr="{}" rfdistance="0"/></anchor></req>'' '.format(addr1_right, addr2_right, addr1_right, addr3_right,addr1_right)

            print("请求的数据：", instruct)
            cls.msg = cls.oder.yq_response(instruct)
            # 断言配置设置未成功标识符status="not connected"已配置

            print("服务器返回的数据：", str(cls.msg, 'utf8'))
            cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(addr1_right),
                         str(cls.msg, 'utf8'))
            print("断言'{}'通过！".format(addr1_right))
            cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(addr2_right),
                         str(cls.msg, 'utf8'))
            print("断言'{}'通过！".format(addr2_right))
            cls.assertIn('<anchor addr="{}" db="config saved" status="config sent"/>'.format(addr3_right),
                         str(cls.msg, 'utf8'))
            print("断言'{}'通过！".format(addr3_right))

# 查询基站列表

    def test003_anchor_list(cls):
        print('查询基站列表:')
        instruct = '<req type="anchor list"/>'  # 指令
        print('请求的数据：{}'.format(instruct))
        cls.msg = cls.oder.yq_response(instruct)
        cls.assertIn('<ind type="anchor list">', str(cls.msg, 'utf8'))
        print("\n服务器第{}次返回的数据：", str(cls.msg, 'utf8'))
        print("断言'基站查询'通过！")

# 对查询基站列表指令进行1000次重复

    def test004_anchor_list(cls):
        i = 1
        print('即将进行10000次的查询基站列表:')
        print('请求的数据：<req type="anchor list"/>')
        while i < 1001:
            instruct = '<req type="anchor list"/>'  # 指令

            cls.msg = cls.oder.yq_response(instruct)

            print("\n服务器第{}次返回的数据：".format(i), str(cls.msg, 'utf8'))
            cls.assertIn('<ind type="anchor list">', str(cls.msg, 'utf8'))
            print("断言'基站查询'通过！{}".format(i))
            i += 1

# 定位算法配置命令

    def test005_anchor_multilateration(cls):
        print('定位算法配置命令:')
        # 指令
        instruct = '<req type="multilateration" algorithm="3"/>'
        print("请求的数据：", instruct)
        cls.msg = cls.oder.yq_response(instruct)
        print("服务器返回的数据：", str(cls.msg, 'utf8'))
        # 断言响应
        cls.assertIn('<ind type="multilateration"/>', str(cls.msg, 'utf8'))
        print("断言'定位算法配置命令'通过！")

# 双向测距

    def test006_ranging_test(cls):
        print('双向测距:')
        instruct = '<req type="range test" num_ranges="100" res_delay="" fin_delay="" reverse="1"><anchor addr = "1aa6083cf920a17"/><anchor addr = "1aa6083cf920913"/><anchor addr = "1aa6083cf91cb9d"/> </req>'
        # instruct = ' < req   type = "range test"     num_ranges = "100" > < anchor        addr = "1aa6083cf92080a" / > < anchor        addr = "1aa6083cf920913" / > < anchor        addr = "1aa6083cf91cb9d" / > < anchor        addr = "1aa6083cf920a17" / > < / req >'
        print("请求的数据：", instruct)
        cls.msg = cls.oder.yq_response2(instruct)
        a = 0
        for i in cls.msg:
            print("服务器返回的数据{}：".format(a), i)
            a += 1
        # 断言响应
        cls.assertIn('<ind type="system status" msg="range measurement completes"></ind>', str(cls.msg))
        print("断言'双向测距'通过！")

# 开始定位

    def test007_start_positioning(cls):
        print('开始定位:')
        instruct = '<req type="rtls start"></req>'  # 指令
        print("请求的数据：", instruct)
        cls.msg = cls.oder.yq_response(instruct)

        print("服务器返回的数据：", str(cls.msg, 'utf8'))
        time.sleep(10)
        cls.assertIn('<ind type="rtls start"/>', str(cls.msg, 'utf8'))  # 断言
        print("断言'开始定位'通过！")

# 开始定位后查询定位状态

    def test008_rtls_start_status(cls):
        print('开始定位后查询定位状态:')
        instruct = '<req type="rtls state"/>'  # 指令
        print("请求的数据：", instruct)
        cls.msg = cls.oder.yq_response(instruct)

        print("服务器返回的数据：", str(cls.msg, 'utf8'))
        time.sleep(10)
        cls.assertIn('<ind type="rtls state" state="running"/>', str(cls.msg, 'utf8'))  # 断言
        print("断言'开始定位后查询定位状态'通过！")

# 停止定位

    def test009_Stop_positioning(cls):
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

# 停止定位后查询定位状态

    def test010_rtls_stop_start(cls):
        print('停止定位后查询定位状态:')
        instruct = '<req type="rtls state"/>'  # 指令
        print("请求的数据：", instruct)
        cls.msg = cls.oder.yq_response(instruct)

        print("服务器返回的数据：", str(cls.msg, 'utf8'))

        cls.assertIn('<ind type="rtls state" state="stopped"/>', str(cls.msg, 'utf8'))  # 断言
        print("断言'停止定位后查询定位状态'通过！")
# 定位天线延迟配置

    def test011_antenna_cfg(cls):
        print('定位天线延迟配置:')
        # 其中count是发送测试数据包的次数，1~65535；period是每次发送的间隔，单位毫秒ms，0~255
        instruct = '<req type="antenna cfg"><anchor addr="1aa6083cf920a17" ant_delay_rx="16492" ant_delay_tx="16492"/><anchor addr="1aa6083cf920913" ant_delay_rx="16492" ant_delay_tx="16492"/><anchor addr="1aa6083cf91cb9d" ant_delay_rx="16492" ant_delay_tx="16492"/></req>'  # 指令

        print("请求的数据：", instruct)
        cls.msg = cls.oder.yq_response(instruct)


        cls.assertIn('status="config sent"', str(cls.msg))  # 断言
        print("断言'定位天线延迟配置'通过！")
# 射频配置命令

    def test012_rf_cfg(cls):
        print('射频配置命令:')
        # 其中count是发送测试数据包的次数，1~65535；period是每次发送的间隔，单位毫秒ms，0~255
        instruct = '<req type="rf cfg"><rf chan="2" prf="64" rate="6810" code="9" plen="128" pac="8" nsfd="0"/></req>'  # 指令

        print("请求的数据：", instruct)
        cls.msg = cls.oder.yq_response(instruct)


        cls.assertIn('status="config sent"', str(cls.msg))  # 断言
        print("断言'射频配置命令'通过！")

# 启用通信测试命令

    def test013_comm_test(cls):
        print('启用通信测试命令:')
        # 其中count是发送测试数据包的次数，1~65535；period是每次发送的间隔，单位毫秒ms，0~255
        instruct = '<req type="comm test" count="100" period="10"><anchor addr = "1aa6083cf920a17" /><anchor addr = "1aa6083cf920913" /></req>'  # 指令

        print("请求的数据：", instruct)
        cls.msg = cls.oder.yq_response2(instruct)

        a = 0
        for i in cls.msg:
            print("服务器返回的数据{}：".format(a), i)
            a += 1

        cls.assertIn('msg="comm test completes">', str(cls.msg))  # 断言
        print("断言'启用通信测试命令'通过！")

# 启用通信测试命令:--基站全部离线状态

    def test014_comm_test_error(cls):
            print('启用通信测试命令:--基站全部离线状态')
            # 其中count是发送测试数据包的次数，1~65535；period是每次发送的间隔，单位毫秒ms，0~255
            instruct = '<req type="comm test" count="100" period="10"><anchor addr = "1aa6083cf92080ab" /><anchor addr = "1aa6083cf920917" /></req>'  # 指令
            # duration是次序发送连续帧的时长 单位秒
            print("请求的数据：", instruct)
            cls.msg = cls.oder.yq_response2(instruct)

            a = 0
            for i in cls.msg:
                print("服务器返回的数据{}：".format(a), i)
                a += 1

            cls.assertNotIn('status="comm test done"', str(cls.msg))  # 断言响应里没有成功的状态
            print("断言'启用通信测试命令'通过！")

# 启用通信测试命令: --基站3个在线状态只有一个离线状态

    def test015_comm_test_error(cls):
            # 其中count是发送测试数据包的次数，1~65535；period是每次发送的间隔，单位毫秒ms，0~255
            addr_error="1aa6083cf920914"
            addr1 = "1aa6083cf91cb9d"
            addr2 = "1aa6083cf920a17"
            addr3 = "1aa6083cf920913"
            print('启用通信测试命令:--基站三个在线状态[{},{},{}]一个离线状态[{}]'.format(addr1,addr2,addr3,addr_error))

            instruct = '<req type="comm test" count="100" period="10">' \
                       '<anchor addr = "{}" /><anchor addr = "{}" />' \
                       '<anchor addr = "{}" /><anchor addr = "{}" /></req>'.format(addr1,addr2,addr3,addr_error)  # 指令

            print("请求的数据：", instruct)
            cls.msg = cls.oder.yq_response2(instruct)

            a = 0
            for i in cls.msg:
                print("服务器返回的数据{}：".format(a), i)
                a += 1
            cls.assertIn('<ind type="comm test"><transmitter addr="1aa6083cf91cb9d"><resp status="comm test done"/>', str(cls.msg))  # 断言  # 断言响应里成功的状态
            cls.assertIn('<ind type="comm test"><transmitter addr="1aa6083cf920913"><resp status="comm test done"/>', str(cls.msg))  # 断言  # 断言响应里成功的状态

            cls.assertIn('<ind type="comm test"><transmitter addr="1aa6083cf920a17"><resp status="comm test done"/>', str(cls.msg))  # 断言  # 断言响应里成功的状态
            cls.assertIn('<ind type="comm test"><transmitter addr="1aa6083cf920914"><resp status="not connected"/>', str(cls.msg))  # 断言 # 断言响应里没有成功的状态
            print("断言启用通信测试命令:--基站三个在线状态[{},{},{}]一个离线状态[{}]状态全部通过".format(addr1,addr2,addr3,addr_error))

# 启用功率测试

    def test016_power_test(cls):
        print('启用功率测试:')
        instruct = '<req type="power test" duration="1"><anchor addr = "1aa6083cf920a17" /><anchor addr = "1aa6083cf920913" /><anchor addr = "1aa6083cf91cb9d" /></req>'  # 指令
        # duration是次序发送连续帧的时长 单位秒
        print("请求的数据：", instruct)
        cls.msg = cls.oder.yq_response3(instruct,6)
        # print(cls.msg)
        a = 0
        for i in cls.msg:
            print("服务器返回的数据{}：".format(a), i)
            a += 1

        cls.assertIn('status="power test done"', str(cls.msg))  # 断言
        print("断言'启用功率测试'通过！")

# 启用功率测试--基站adrr有一个出现错误或者离线时

    def test017_power_test_error1(cls):
        addr='1aa6083cf920a17'
        addr_error1='1aa6083cf920914'
        addr_error2 = '1aa6083cf91cb9e'
        print('启用功率测试--基站adrr【1aa6083cf920a17】有一个在线，其他基站都出现错误或者离线时:')
        instruct = '<req type="power test" duration="1"><anchor addr="1aa6083cf920a17"  /><anchor addr = "1aa6083cf920914" /><anchor addr = "1aa6083cf91cb9e" /></req>'  # 指令
        print("请求的数据：", instruct)
        cls.msg = cls.oder.yq_response3_error(instruct)

        a = 0
        for i in cls.msg:
            print("服务器返回的数据{}：".format(a), i)
            a += 1
        cls.assertIn('<ind type="power test" addr="{}" status="power test done"/></ind>'.format(addr), str(cls.msg))  # 断言
        print("断言'启用功率测试--在线的基站{}测试'通过！".format(addr))
        cls.assertIn('status="not connected"', str(cls.msg))  # 断言
        print("断言'启用功率测试--离线的基站adrr{}，{}测试'通过！".format(addr_error1,addr_error2))

# 启用功率测试--基站adrr全部出现错误或者离线时

    def test018_power_test_error2(cls):
            print('启用功率测试--基站adrr全部出现错误或者离线时:')
            instruct = '    print("请求的数据：",<req type="power test" duration="1"><anchor addr = "1aa6083cf920a19" /><anchor addr = "1aa6083cf920914" /><anchor addr = "1aa6083cf91cb9e" /></req>'  # 指令
    #          instruct)
            cls.msg = cls.oder.yq_response3_error(instruct)
            a = 0
            for i in cls.msg:
                print("服务器返回的数据{}：".format(a), i)
                a += 1

            cls.assertIn('status="not connected"',str(cls.msg))   # 断言
            print("断言'启用功率测试--基站adrr出现错误或者离线时'通过！")

# 指定基站重启

    def test019_reset_appoint_anchor(cls):
        print('指定基站addr=1aa6083cf920913:重启')
        instruct = '<req type="anchor reset"><anchor addr = "1aa6083cf920913" /></req>'  # 指令
        print("请求的数据：", instruct)
        cls.msg = cls.oder.yq_response(instruct)
        print("服务器返回的数据：", str(cls.msg, 'utf8'))
        cls.assertIn('<ind type="anchor reset"/>', str(cls.msg, 'utf8'))  # 断言
        print("断言'重启指定基站'通过！")
# 重启全部基站

    def test020_reset_anchor(cls):
        print('重启全部基站:')
        instruct = '<req type="anchor reset"/>'  # 指令
        print("请求的数据：", instruct)
        cls.msg = cls.oder.yq_response(instruct)

        print("服务器返回的数据：", str(cls.msg, 'utf8'))


        print("断言'重启全部基站'通过！")

# 诊断信息配置命令

    def test021_log_cfg(cls):
        print('诊断信息配置命令:')
        instruct = '<req type="log cfg"><anchor addr="1aa6083cf920a17" rxdiag_on="1" accum_on="1" accum_type="1"/><anchor addr="1aa6083cf920913" rxdiag_on="0" accum_on="0" accum_type="0"/><anchor addr="1aa6083cf91cb9d" rxdiag_on="0" accum_on="0" accum_type="0"/></req>'  # 指令
        print("请求的数据：", instruct)
        cls.msg = cls.oder.yq_response(instruct)

        print("服务器返回的数据：", str(cls.msg, 'utf8'))

        cls.assertIn(' status="config sent"', str(cls.msg, 'utf8'))  # 断言
        print("断言'诊断信息配置命令'通过！")

