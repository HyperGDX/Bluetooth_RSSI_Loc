import parse
from cal_func import *


def cal_one_object_top_n(rssis, top_n=parse.Top_N):
    rssis = rssi_check_positive(rssis)
    # lst转np.nd
    rssi_nd = np.array(rssis)
    # 取所有rssi大小顺序的下标
    rssi_nd_all_argsort = np.argsort(rssi_nd)
    # 截取前TOPN个
    rssi_nd_topn_idx = rssi_nd_all_argsort[0:top_n]
    rssi_nd_topn = rssi_nd[rssi_nd_topn_idx]
    return rssi_nd_topn_idx, rssi_nd_topn


def gen_circles_parse(rssi_lst, beacon_loc_lst, up_rate=1.0):
    circles_parse = []
    for i in range(len(beacon_loc_lst)):
        circles_parse.append([beacon_loc_lst[i], rssi2d(rssi_lst[i]) * up_rate])
    return circles_parse
