import os

import unit
from api.jzyq_api import Test_api
import unittest
import time
class  anchor_cfgs():
    def __init__(self):
        self.response=Test_api()
#对四个基站配置
    def anchor_cfg(self,json1,json2,json3,json4):

        print('基站进行配置命令:')

        addr1 = json1[0][0]  # 定位基站的64位唯一标识
        syncref1 = json1[0][1]  # 1 – 作为时间同步参考的基站, 0 – 非参考
        follow_addr1 = json1[0][2]  # 本基站作为时间同步参考点时，发送CCP需要在follow_addr基站之后，如果是0或者是自身，则该基站自主发送CCP
        lag_delay1 = json1[0][3]  # 本基站作为时间同步参考点时，发送CCP相对于follow_addr基站CCP的接收时间戳的延时，单位μs（微秒），0~4294967295
        syncrefanchor_addr1 = json1[0][4]  # 本基站与该地址的时间同步参考基站进行时间同步
        syncrefanchor_rfdistance1 = json1[0][5]  # 本基站与时间同步参考基站的距离，单位米m，如果是0，则使用几何距离
        x1 = json1[0][6]  # X坐标值，单位米m
        y1 = json1[0][7]  # Y坐标值，单位米m
        z1 = json1[0][8]  # Z坐标值，单位米m

        addr2 = json2[0][0]  # 定位基站的64位唯一标识
        syncref2 = json2[0][1]  # 1 – 作为时间同步参考的基站, 0 – 非参考
        follow_addr2 = json2[0][2]  # 本基站作为时间同步参考点时，发送CCP需要在follow_addr基站之后，如果是0或者是自身，则该基站自主发送CCP
        lag_delay2 = json2[0][3]  # 本基站作为时间同步参考点时，发送CCP相对于follow_addr基站CCP的接收时间戳的延时，单位μs（微秒），0~4294967295
        syncrefanchor_addr2 = json2[0][4]  # 本基站与该地址的时间同步参考基站进行时间同步
        syncrefanchor_rfdistance2 = json2[0][5]  # 本基站与时间同步参考基站的距离，单位米m，如果是0，则使用几何距离
        x2 = json2[0][6]  # X坐标值，单位米m
        y2 = json2[0][7]  # Y坐标值，单位米m
        z2 = json2[0][8]  # Z坐标值，单位米m

        addr3 = json3[0][0]  # 定位基站的64位唯一标识
        syncref3 = json3[0][1]  # 1 – 作为时间同步参考的基站, 0 – 非参考
        follow_addr3 = json3[0][2]  # 本基站作为时间同步参考点时，发送CCP需要在follow_addr基站之后，如果是0或者是自身，则该基站自主发送CCP
        lag_delay3 = json3[0][3]  # 本基站作为时间同步参考点时，发送CCP相对于follow_addr基站CCP的接收时间戳的延时，单位μs（微秒），0~4294967295
        syncrefanchor_addr3 = json3[0][4]  # 本基站与该地址的时间同步参考基站进行时间同步
        syncrefanchor_rfdistance3 = json3[0][5]  # 本基站与时间同步参考基站的距离，单位米m，如果是0，则使用几何距离
        x3 = json3[0][6]  # X坐标值，单位米m
        y3 = json3[0][7]  # Y坐标值，单位米m
        z3 = json3[0][8]  # Z坐标值，单位米m

        addr4 = json4[0][0]  # 定位基站的64位唯一标识
        syncref4 = json4[0][1]  # 1 – 作为时间同步参考的基站, 0 – 非参考
        follow_addr4 = json4[0][2]  # 本基站作为时间同步参考点时，发送CCP需要在follow_addr基站之后，如果是0或者是自身，则该基站自主发送CCP
        lag_delay4 = json4[0][3]  # 本基站作为时间同步参考点时，发送CCP相对于follow_addr基站CCP的接收时间戳的延时，单位μs（微秒），0~4294967295
        syncrefanchor_addr4 = json4[0][4]  # 本基站与该地址的时间同步参考基站进行时间同步
        syncrefanchor_rfdistance4 = json4[0][5]  # 本基站与时间同步参考基站的距离，单位米m，如果是0，则使用几何距离
        x4 = json4[0][6]  # X坐标值，单位米m
        y4 = json4[0][7]  # Y坐标值，单位米m
        z4 = json4[0][8]  # Z坐标值，单位米m

        instruct='<req type="anchor cfg"><anchor addr="{}" syncref="{}" follow_addr="{}" lag_delay="{}" x="{}" y="{}" z="{}"  ></anchor><anchor addr="{}" syncref="{}" follow_addr="{}" lag_delay="{}" x="{}" y="{}" z="{}" ><syncrefanchor addr="{}" rfdistance="{}"/></anchor><anchor addr="{}" syncref="{}" follow_addr="{}" lag_delay="{}" x="{}" y="{}" z="{}" ><syncrefanchor addr="{}" rfdistance="{}"/><syncrefanchor addr="{}" rfdistance="{}"/></anchor><anchor addr="{}" syncref="{}" follow_addr="{}" lag_delay="{}" x="{}" y="{}" z="{}" ><syncrefanchor addr="{}" rfdistance="{}"/><syncrefanchor addr="{}" rfdistance="{}"/></anchor></req>'.format(addr1,syncref1,follow_addr1,lag_delay1,x1,y1,z1,
                          addr2, syncref2, follow_addr2, lag_delay2, x2, y2, z2,syncrefanchor_addr1,syncrefanchor_rfdistance1,
                          addr3, syncref3, follow_addr3, lag_delay3, x3, y3, z3, syncrefanchor_addr1,
                          syncrefanchor_rfdistance1,syncrefanchor_addr2,syncrefanchor_rfdistance2,
                          addr4, syncref4, follow_addr4, lag_delay4, x4, y4, z4, syncrefanchor_addr2,
                          syncrefanchor_rfdistance2, syncrefanchor_addr3, syncrefanchor_rfdistance3
                          )

        print("请求的数据：", instruct)

        self.msg = self.response.yq_response(instruct=instruct)

        return self.msg

#对单个基站配置
    def anchor_cfg_one(self, json1):
        print('基站进行配置命令:')

        addr1 = json1[0][0]  # 定位基站的64位唯一标识
        syncref1 = json1[0][1]  # 1 – 作为时间同步参考的基站, 0 – 非参考
        follow_addr1 = json1[0][2]  # 本基站作为时间同步参考点时，发送CCP需要在follow_addr基站之后，如果是0或者是自身，则该基站自主发送CCP
        lag_delay1 = json1[0][3]  # 本基站作为时间同步参考点时，发送CCP相对于follow_addr基站CCP的接收时间戳的延时，单位μs（微秒），0~4294967295
        syncrefanchor_addr1 = json1[0][4]  # 本基站与该地址的时间同步参考基站进行时间同步
        syncrefanchor_rfdistance1 = json1[0][5]  # 本基站与时间同步参考基站的距离，单位米m，如果是0，则使用几何距离
        x1 = json1[0][6]  # X坐标值，单位米m
        y1 = json1[0][7]  # Y坐标值，单位米m
        z1 = json1[0][8]  # Z坐标值，单位米m


        instruct = '<req type="anchor cfg"><anchor addr="{}" syncref="{}" follow_addr="{}" lag_delay="{}" x="{}" y="{}" z="{}" >' \
                   '<syncrefanchor addr="{}" rfdistance="{}"/>' \
                   '</anchor></req>'.format(
        addr1, syncref1, follow_addr1, lag_delay1, x1, y1, z1,syncrefanchor_addr1,syncrefanchor_rfdistance1)

        print("请求的数据：", instruct)

        self.msg = self.response.yq_response(instruct=instruct)

        return self.msg