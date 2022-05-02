import read_data
import numpy as np
import parse
from cal_func import cal_d


def cal_one_object_top_n(rssi_lst):
    """
    计算单个物体的topn
    :param rssi_lst: 正值
    :return: 返回topn_idx,topn
    """
    # lst转np.nd
    rssi_nd = np.array(rssi_lst)
    # 取所有rssi大小顺序的下标
    rssi_nd_all_argsort = np.argsort(rssi_nd)
    # 截取前TOPN个
    rssi_nd_topn_idx = rssi_nd_all_argsort[0:parse.Top_N]
    rssi_nd_topn = rssi_nd[rssi_nd_topn_idx]
    # [3 2 1 0]
    # [83.1766 80.9921 77.9977 73.2114]
    return rssi_nd_topn_idx, rssi_nd_topn


def gen_circles_parse(rssi_lst, up_rate=1.0):
    """
    生成单个物体的圆数据
    :param rssi_lst: 正值
    :param up_rate: 增幅
    :return:
    """
    topn_idx, topn_rssi = cal_one_object_top_n(rssi_lst)
    circles_parse = []
    for i in range(len(topn_idx)):
        circles_parse.append([read_data.beacon_loc_lst_tuple[topn_idx[i]],
                              cal_d(topn_rssi[i]) * up_rate])
    return circles_parse

# tt = get_one_rssi_nd(0)
# print(tt)
# ttt = gen_circles_parse(tt)
# print(ttt)
# [[(0, 0), 5.073235234009597],
#  [(0, 10), 6.682554355985489],
#  [(10, 0), 7.939670876986527],
#  [(10, 10), 9.00357527770025]]
