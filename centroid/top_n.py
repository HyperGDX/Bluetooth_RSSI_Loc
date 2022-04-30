import gen_rssi
import numpy as np
from scipy import ndimage

# m个基站
b_ls = gen_rssi.b_ls
# n个待测
o_ls = gen_rssi.o_ls


# 获取基站坐标并返回
def get_beacon_locs():
    pass


# 获取待测物体坐标并返回
def get_object_locs():
    pass


# 计算基站和待测目标之间的RSSI
# n*m
test_rssi_lsts = gen_rssi.cal_rssis(b_ls, o_ls)
# print(test_rssi)
# [[-73.2114, -77.9977, -80.9921, -83.1766, -60.1057],
# [-81.825, -79.1751, -79.1751, -75.2216, -52.6443]]

# 选前几的基站数据
Top_N = 4


def cal_one_object_top_n(rssi_lst):
    """
    :param rssi_lst: 输入单个待测物体对所有基站的rssi(1xm)
    :return: 返回topn_idx,topn
    """
    # lst转np.nd
    rssi_nd = np.array(rssi_lst)
    rssi_nd = -rssi_nd
    # [73.2114 77.9977 80.9921 83.1766 60.1057]

    # 取所有rssi大小顺序的下标
    rssi_nd_all_argsort = np.argsort(rssi_nd)[::-1]
    # [4 0 1 2 3]


    # 截取前TOPN个
    rssi_nd_topn_idx = rssi_nd_all_argsort[0:Top_N]
    rssi_nd_topn = rssi_nd[rssi_nd_topn_idx]
    # print(rssi_nd_topn, rssi_nd_topn_idx)
    # [60.1057 73.2114 77.9977 80.9921]
    # [4 0 1 2]
    return rssi_nd_topn_idx, rssi_nd_topn


idx, topn = cal_one_object_top_n(test_rssi_lsts[0])
# [60.1057 73.2114 77.9977 80.9921]
# [4 0 1 2]



# A = -45
# n = 4
#
# test_rssi_d_n_max = []
# for rssi in test_rssi_n_max:
#     d = 10 ** ((A - rssi) / (10 * n))
#     test_rssi_d_n_max.append(d)
#
# for i in range(len(test_rssi_n_max)):
#     print(gen_rssi.cal_dist((3, 4), b_ls[i]))
